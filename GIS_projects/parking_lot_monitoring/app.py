import cv2
import pandas as pd
import numpy as np
import serial
import time
import json
import os
import arcpy
import psycopg2
import threading
from util import get_parking_spots_bboxes, empty_or_not

def calc_diff(im1, im2):
    return np.abs(np.mean(im1) - np.mean(im2))

# PostgreSQL Database Connection Parameters
DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "pass@6454439",
    "host": "localhost",
    "port": "5432"
}

DB_NAME = "parking_db"

def create_database():
    """Creates a new database if it doesn't exist."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
        exists = cur.fetchone()

        if not exists:
            cur.execute(f"CREATE DATABASE {DB_NAME};")
            print(f"✅ Database '{DB_NAME}' created successfully!")
        else:
            print(f"ℹ️ Database '{DB_NAME}' already exists.")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error creating database: {e}")

def create_table():
    """Creates a table in the database."""
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user="postgres", password="pass@6454439", host="localhost", port="5432")
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS parking_spots (
                Id VARCHAR(10) PRIMARY KEY,
                Status VARCHAR(10)
            );
        """)
        conn.commit()
        print("✅ Table 'parking_spots' created successfully!")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error creating table: {e}")

# Function to update PostgreSQL with the parking spot statuses
def update_parking_status(db_data):
    """Updates the parking status in the database efficiently using batch insert."""
    if not db_data:
        print("⚠️ No data to update.")
        return

    try:
        conn = psycopg2.connect(dbname=DB_NAME, user="postgres", password="pass@6454439", host="localhost", port="5432")
        cur = conn.cursor()

        sql = """
        INSERT INTO parking_spots (Id, Status)
        VALUES %s
        ON CONFLICT (Id) DO UPDATE SET Status = EXCLUDED.Status;
        """
        
        # Use psycopg2's execute_values to insert all records at once
        from psycopg2.extras import execute_values
        execute_values(cur, sql, db_data)

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Database updated successfully!")

    except Exception as e:
        print("❌ Error updating database:", e)

def update_parking_status_async(db_data):
    """Runs the update in a separate thread."""
    threading.Thread(target=update_parking_status, args=(db_data,)).start()

# Load mask and video
mask = 'mask_1920_1080.png'
video_path = 'parking_1920_1080_loop.mp4'
mask = cv2.imread(mask, 0)
cap = cv2.VideoCapture(video_path)

# Extract parking spots
connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
spots = get_parking_spots_bboxes(connected_components)

# Sort spots by x-coordinates (columns)
spots = sorted(spots, key=lambda x: x[0])

# Categorize into columns and rows
column_threshold = 50
columns = []
current_column = []
last_x = spots[0][0]

for spot in spots:
    x, y, w, h = spot
    if abs(x - last_x) > column_threshold:
        columns.append(current_column)
        current_column = []
    current_column.append(spot)
    last_x = x

columns.append(current_column)

# Sort each column by y-coordinates (rows)
for column in columns:
    column.sort(key=lambda x: x[1])

# Generate column labels from A, B, C, ...
def get_column_label(col_idx):
    """Generate column labels like A, B, ..., Z, AA, AB, ..."""
    label = ""
    while col_idx >= 0:
        label = chr(ord('A') + (col_idx % 26)) + label
        col_idx = (col_idx // 26) - 1
    return label


# Label the spots by column and row
labelled_spots = []
for col_idx, column in enumerate(columns):
    for row_idx, spot in enumerate(column):
        labelled_spots.append((get_column_label(col_idx), row_idx + 1, spot))

spots_status = [None for _ in spots]
diffs = [None for _ in spots]

previous_frame = None
previous_spots_status = [None] * len(spots)

frame_nmr = 0
ret = True
step = 60

# Serial communication setup (Kept but not executed)
#ser = serial.Serial('COM3', 115200)  # Adjust 'COM3' to your serial port
#time.sleep(2)  # Wait for the serial connection to initialize

csv_file = r"D:\my_work\personal_projects\ai_projects\parking_lot_monitoring\arcgis_layers\parking_status.csv"

# Ensure CSV file exists
if not os.path.exists(csv_file):
    pd.DataFrame(columns=["Id", "Status"]).to_csv(csv_file, index=False)
    print(f"Empty CSV file created: {csv_file}")

previous_db_update = []

try:
    while ret:
        ret, frame = cap.read()

        if frame_nmr % step == 0 and previous_frame is not None:
            for spot_indx, spot_info in enumerate(labelled_spots):
                col, row, spot = spot_info
                x1, y1, w, h = spot

                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]

                diffs[spot_indx] = calc_diff(spot_crop, previous_frame[y1:y1 + h, x1:x1 + w, :])

            print("Differences between current and previous frame calculated for all spots.")

        if frame_nmr % step == 0:
            if previous_frame is None:
                arr_ = range(len(spots))
            else:
                arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4]
            for spot_indx in arr_:
                col, row, spot = labelled_spots[spot_indx]
                x1, y1, w, h = spot

                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]

                spot_status = empty_or_not(spot_crop)

                spots_status[spot_indx] = spot_status

        if frame_nmr % step == 0:
            previous_frame = frame.copy()

            # Check if parking spots' status has changed
            if spots_status != previous_spots_status:
                column_counts = {get_column_label(i): 0 for i in range(len(columns))}
        
                for spot_indx, spot_info in enumerate(labelled_spots):
                    col, row, spot = spot_info
                    if spots_status[spot_indx]:  # If spot is empty
                        column_counts[col] += 1
        
                # Store the last known spot statuses
                previous_spots_status = spots_status.copy()

        # Update CSV in real-time
        updated_data = []
        for spot_indx, spot_info in enumerate(labelled_spots):
            col, row, spot = spot_info
            spot_status = "Empty" if spots_status[spot_indx] else "Occupied"
            spot_id = f"{col}{row}"
            updated_data.append({"Id": spot_id, "Status": spot_status})

        if updated_data:
            df = pd.DataFrame(updated_data, columns=["Id", "Status"])
            df.to_csv(csv_file, index=False)
        else:
            print("⚠️ No data to write to CSV. Skipping DataFrame creation.")
        
        # Prepare data for PostgreSQL
        updated_data = []
        for spot_indx, spot_info in enumerate(labelled_spots):
            col, row, spot = spot_info
            spot_status = "Empty" if spots_status[spot_indx] else "Occupied"
            spot_id = f"{col}{row}"  # Ensure correct ID format
            updated_data.append((spot_id, spot_status))

        # ✅ **FIX: Add this to avoid NameError**
        if previous_spots_status is None:
            previous_spots_status = spots_status.copy()

        # ✅ **Only update DB if a significant number of spots changed**
        if frame_nmr % step == 0:
        # Calculate changed spots
            changed_spots = [(spot_id, spot_status) for spot_id, spot_status in updated_data if (spot_id, spot_status) not in previous_db_update]

        # Only update if a significant number of spots changed
            if len(changed_spots) > 5:  # Adjust the threshold as needed
                update_parking_status_async(changed_spots)
                previous_db_update = changed_spots.copy()  # Store last updated spots
            previous_spots_status = [s if s is not None else False for s in spots_status] # Store last state
        
        # Debugging print
        #print("📌 Data being sent to DB:", updated_data[:5])  # Print first 5 records

        # Update PostgreSQL
        if updated_data and updated_data != previous_db_update:
            update_parking_status_async(updated_data)
            previous_db_update = updated_data.copy()


        # Draw bounding boxes and labels
        for spot_indx, spot_info in enumerate(labelled_spots):
            col, row, spot = spot_info
            x1, y1, w, h = spot
            color = (0, 255, 0) if spots_status[spot_indx] else (0, 0, 255)
            cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), color, 2)
            label = f"{col}{row}"
            if col in 'ACEGIKMO':
                cv2.putText(frame, label, (x1 - 30, y1 + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            else:
                cv2.putText(frame, label, (x1 + w + 5, y1 + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
         # Draw the available spots text with adjustable position and size
        def draw_text_box(frame, text, pos, font, scale, color, thickness):
            (text_width, text_height), baseline = cv2.getTextSize(text, font, scale, thickness)
            x, y = pos
            # Draw background rectangle
            cv2.rectangle(frame, (x, y - text_height - baseline), (x + text_width, y + baseline), (0, 0, 0), -1)
            # Draw text
            cv2.putText(frame, text, (x, y), font, scale, color, thickness)

        text = 'Available spots: {} / {}'.format(str(sum(spots_status)), str(len(spots_status)))
        text_x, text_y = 40, 60  # Specify the position here
        draw_text_box(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

      # Define custom Y-offsets for each column
        column_y_offsets = {
        'A': -280, 'B': -25, 'C': -30, 'D': -15,  # Adjust as needed
        'E': -10, 'F': -12, 'G': -18, 'H': -24,
        'I': -20, 'J': -22, 'K': -18, 'L': -24,
        'M': -10, 'N': -12, 'O': -15, 'P': -20
        }
        # Draw column counts above each column
        for col_idx, column in enumerate(columns):
            col_label = get_column_label(col_idx)
            count_label = f"{column_counts[col_label]}"
            if column:
                x1, y1, w, h = column[0]
                count_pos = (x1 + w // 2, y1 - 10 - (col_idx * 5))
                
                # Apply per-column Y offset (default to -10 if column isn't in dictionary)
                
                y_offset = column_y_offsets.get(col_label, -10)
                count_pos = (x1 + w // 2, y1 + y_offset)

                # Draw green box for count label
                count_text_size = cv2.getTextSize(count_label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
                box_x1, box_y1 = count_pos[0], count_pos[1] - count_text_size[1] - 2
                box_x2, box_y2 = count_pos[0] + count_text_size[0] + 5, count_pos[1] + 5
                cv2.rectangle(frame, (box_x1, box_y1), (box_x2, box_y2), (0, 255, 0), -1)
                cv2.putText(frame, count_label, count_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
                
                """# Insert bounding boxes into the shapefile
                with arcpy.da.InsertCursor(output_shp, ["SHAPE@", "Column", "Row"]) as cursor:
                    for col, row, spot in labelled_spots:
                        x1, y1, w, h = spot
                        x2, y2 = x1 + w, y1 + h

                # Create polygon geometry with Y-axis flipped
                    y1, y2 = -y1, -y2  # Flip Y-coordinates

                    polygon = arcpy.Polygon(arcpy.Array([arcpy.Point(x1, y1),
                                             arcpy.Point(x2, y1),
                                             arcpy.Point(x2, y2),
                                             arcpy.Point(x1, y2),
                                             arcpy.Point(x1, y1)]),
                                            spatial_ref)

                    cursor.insertRow([polygon, col, row])"""

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        frame_nmr += 1

finally:
    cap.release()  # Ensure camera resource is released
    cv2.destroyAllWindows()  # Close any OpenCV windows
    print("Shutdown complete.")
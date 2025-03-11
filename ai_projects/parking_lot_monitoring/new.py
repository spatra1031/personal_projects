import cv2
import pandas as pd
import numpy as np
import psycopg2
import os
import time
from util import get_parking_spots_bboxes, empty_or_not

# PostgreSQL Connection Parameters
DB_PARAMS = {
    "dbname": "parking_db",
    "user": "postgres",
    "password": "pass@6454439",
    "host": "localhost",
    "port": "5432"
}

# Function to update PostgreSQL with the parking spot statuses
def update_parking_status(parking_data):
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        conn.autocommit = True  # 🔹 Enable auto-commit
        cur = conn.cursor()

        # Check current DB state before insertion
        print("📌 Current Data in DB Before Update:")
        cur.execute("SELECT * FROM parking_status;")
        rows = cur.fetchall()
        for row in rows[:5]:  # Print first 5 rows
            print(row)
        
        print("✅ Inserting data into PostgreSQL...")  

        # Insert or update all rows in one query for efficiency
        sql = """
        INSERT INTO parking_status (id, status)
        VALUES %s
        ON CONFLICT (id) DO UPDATE SET status = EXCLUDED.status;
        """

        # Convert data to tuples
        data_tuples = [(spot_id, status) for spot_id, status in parking_data]

        # Use psycopg2's execute_values for batch insert
        from psycopg2.extras import execute_values
        execute_values(cur, sql, data_tuples)

        conn.commit()

        # Check DB state after insertion
        print("📌 Data in DB After Update:")
        cur.execute("SELECT * FROM parking_status;")
        rows = cur.fetchall()
        for row in rows[:5]:  # Print first 5 rows
            print(row)

        cur.close()
        conn.close()
        print("✅ Database updated successfully!")

    except Exception as e:
        print("❌ Error updating database:", e)

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

# Generate column labels
def get_column_label(col_idx):
    """Generate column labels like A, B, ..., Z, AA, AB, ..."""
    label = ""
    while col_idx >= 0:
        label = chr(ord('A') + (col_idx % 26)) + label
        col_idx = (col_idx // 26) - 1
    return label

print(f"Generated Column Labels: {[get_column_label(i) for i in range(len(columns))]}")  # Debugging print

# Label the spots by column and row
labelled_spots = []
for col_idx, column in enumerate(columns):
    for row_idx, spot in enumerate(column):
        labelled_spots.append((get_column_label(col_idx), row_idx + 1, spot))

spots_status = [False for _ in spots]  # Fix: Initialize with False instead of None
diffs = [0 for _ in spots]  # Fix: Initialize with 0

previous_frame = None
frame_nmr = 0
ret = True
step = 30

# CSV File Path
csv_file = r"D:\my_work\personal_projects\ai_projects\parking_lot_monitoring\arcgis_layers\parking_status.csv"

# Ensure CSV file exists
if not os.path.exists(csv_file):
    pd.DataFrame(columns=["Id", "Status"]).to_csv(csv_file, index=False)
    print(f"Empty CSV file created: {csv_file}")

try:
    while ret:
        ret, frame = cap.read()

        if frame_nmr % step == 0 and previous_frame is not None:
            for spot_indx, spot_info in enumerate(labelled_spots):
                col, row, spot = spot_info
                x1, y1, w, h = spot
                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]
                diffs[spot_indx] = np.abs(np.mean(spot_crop) - np.mean(previous_frame[y1:y1 + h, x1:x1 + w, :]))

        if frame_nmr % step == 0:
            if previous_frame is None:
                arr_ = range(len(spots))
            else:
                arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4]

            for spot_indx in arr_:
                col, row, spot = labelled_spots[spot_indx]
                x1, y1, w, h = spot
                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]
                spots_status[spot_indx] = empty_or_not(spot_crop)

        if frame_nmr % step == 0:
            previous_frame = frame.copy()

        # Prepare Data (Use same structure for CSV and DB)
        updated_data = [{"Id": f"{col}{row}", "Status": "Empty" if spots_status[spot_indx] else "Occupied"} for spot_indx, (col, row, spot) in enumerate(labelled_spots)]

        # Write to CSV
        if updated_data:
            df = pd.DataFrame(updated_data)
            df.to_csv(csv_file, index=False)

        # Convert CSV format to DB format
        updated_db_data = [(row["Id"], row["Status"]) for row in updated_data]

        # Debug: Print what is being inserted
        print("📌 Data being sent to DB:", updated_db_data[:5])  # Print first 5 records

        # Write to PostgreSQL
        if updated_db_data:
            update_parking_status(updated_db_data)

        frame_nmr += 1

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("Shutdown complete.")

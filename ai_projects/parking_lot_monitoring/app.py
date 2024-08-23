import cv2
import numpy as np
import serial
import time
import json
from util import get_parking_spots_bboxes, empty_or_not

def calc_diff(im1, im2):
    return np.abs(np.mean(im1) - np.mean(im2))

mask = 'mask_1920_1080.png'
video_path = 'parking_1920_1080_loop.mp4'

mask = cv2.imread(mask, 0)

cap = cv2.VideoCapture(video_path)

connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)

spots = get_parking_spots_bboxes(connected_components)

# Sort spots by x-coordinates (columns)
spots = sorted(spots, key=lambda x: x[0])

# Categorize into columns and rows
column_threshold = 50  # Adjust threshold based on your specific case
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

columns.append(current_column)  # Add the last column

# Sort each column by y-coordinates (rows)
for column in columns:
    column.sort(key=lambda x: x[1])

# Generate column labels from A, B, C, ...
def get_column_label(col_idx):
    return chr(ord('A') + col_idx)

# Label the spots by column and row
labelled_spots = []
for col_idx, column in enumerate(columns):
    for row_idx, spot in enumerate(column):
        labelled_spots.append((get_column_label(col_idx), row_idx + 1, spot))

spots_status = [None for _ in spots]
diffs = [None for _ in spots]

previous_frame = None

frame_nmr = 0
ret = True
step = 30

# Define positions for count labels for each column
column_count_positions = {
    'A': (80, 125),
    'B': (190, 125),
    'C': (305, 125),
    'D': (410, 125),
    'E': (530, 90),
    'F': (650, 90),
    'G': (765, 155),
    'H': (885, 155),
    'I': (990, 95),
    'J': (1110, 95),
    'K': (1220, 135),
    'L': (1330, 135),
    'M': (1450, 135),
    'N': (1550, 135),
    'O': (1670, 135),
    'P': (1800, 135) 
}

# Serial communication setup
#ser = serial.Serial('COM3', 115200)  # Adjust 'COM3' to your serial port
#time.sleep(2)  # Wait for the serial connection to initialize

while ret:
    ret, frame = cap.read()

    if frame_nmr % step == 0 and previous_frame is not None:
        for spot_indx, spot_info in enumerate(labelled_spots):
            col, row, spot = spot_info
            x1, y1, w, h = spot

            spot_crop = frame[y1:y1 + h, x1:x1 + w, :]

            diffs[spot_indx] = calc_diff(spot_crop, previous_frame[y1:y1 + h, x1:x1 + w, :])

        print([diffs[j] for j in np.argsort(diffs)][::-1])

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

    # Count empty spots in each column
    column_counts = {get_column_label(i): 0 for i in range(len(columns))}
    for spot_indx, spot_info in enumerate(labelled_spots):
        col, row, spot = spot_info
        if spots_status[spot_indx]:
            column_counts[col] += 1

    # Send the counts to ESP32
    #counts_str = ','.join([f"{col}:{count}" for col, count in column_counts.items()])
    #ser.write(counts_str.encode('utf-8'))
    #ser.write(b'\n')  # End of message

    for spot_indx, spot_info in enumerate(labelled_spots):
        col, row, spot = spot_info
        spot_status = spots_status[spot_indx]
        x1, y1, w, h = spot

        color = (0, 255, 0) if spot_status else (0, 0, 255)
        frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), color, 2)
        
        label = f"{col}{row}"
        if col in 'ACEGIKMO':
            cv2.putText(frame, label, (x1 - 30, y1 + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        else:
            cv2.putText(frame, label, (x1 + w + 5, y1 + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Draw column counts above each column
    for col_idx, column in enumerate(columns):
        col_label = get_column_label(col_idx)
        count_label = f"{column_counts[col_label]}"
        if column:
            x1, y1, w, h = column[0]
            # Get position for count label
            count_pos = column_count_positions.get(col_label, (0, 0))
            # Draw green box for count label
            count_text_size = cv2.getTextSize(count_label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
            box_x1, box_y1 = count_pos[0], count_pos[1] - count_text_size[1] - 2
            box_x2, box_y2 = count_pos[0] + count_text_size[0] + 5, count_pos[1] + 5
            cv2.rectangle(frame, (box_x1, box_y1), (box_x2, box_y2), (0, 255, 0), -1)
            cv2.putText(frame, count_label, count_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

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

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)
    #output_video.write(frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    frame_nmr += 1

cap.release()
cv2.destroyAllWindows()
#ser.close()
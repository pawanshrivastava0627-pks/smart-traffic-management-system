from ultralytics import YOLO
import cv2
from counter import VehicleCounter

# Load YOLO model
model = YOLO("yolov8n.pt")

# Initialize counter
counter = VehicleCounter()

# Load video
video_path = "input/traffic.mp4"
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Unable to open video.")
    exit()

print("Video loaded successfully!")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Vehicle Tracking
    results = model.track(
        frame,
        persist=True,
        verbose=False
    )

    # Get tracking boxes
    boxes = results[0].boxes

    # Count unique vehicles
    if boxes.id is not None:
        track_ids = boxes.id.int().cpu().tolist()

        for box, track_id in zip(boxes.xyxy, track_ids):

         x1, y1, x2, y2 = box

         center_y = int((y1 + y2) / 2)

         counter.should_count(track_id, center_y)

    # Draw detections
    annotated_frame = results[0].plot()

    # Draw virtual counting line
    cv2.line(
        annotated_frame,
        (0, 400),
        (1280, 400),
        (0, 255, 0),
        3
    )

    # Display total vehicle count
    cv2.putText(
        annotated_frame,
        f"Total Vehicles: {counter.count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # Show output
    cv2.imshow("Smart Traffic Management System", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
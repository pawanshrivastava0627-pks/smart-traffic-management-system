from ultralytics import YOLO
import cv2
from counter import VehicleCounter

# Load YOLO model
model = YOLO("yolov8n.pt")

counter = VehicleCounter()

# Load video
video_path = "input/traffic.mp4"
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Unable to open video.")
    exit()

print("Video loaded successfully!")
frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(
        frame,
        persist=True,
        verbose=False
    )
    boxes = results[0].boxes

    if boxes.id is not None:
     boxes = results[0].boxes

     if boxes.id is not None:

      track_ids = boxes.id.int().cpu().tolist()

      for track_id in track_ids:
        counter.count_vehicle(track_id)

      print("Total Vehicles:", counter.count)

    annotated_frame = results[0].plot()

    cv2.imshow("Traffic Video", annotated_frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

class VehicleCounter:

    def __init__(self):
        self.count = 0
        self.counted_ids = set()

    def count_vehicle(self, track_id):
        if track_id not in self.counted_ids:
            self.count += 1
            self.counted_ids.add(track_id)

        return self.count
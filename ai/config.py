# Video Configuration
VIDEO_PATH = "input/traffic.mp4"

# YOLO Model
MODEL_NAME = "yolov8n.pt"

# Counting Line
LINE_Y = 400
LINE_COLOR = (0, 255, 0)
LINE_THICKNESS = 3

# Display Text
TEXT_POSITION = (20, 50)
TEXT_COLOR = (0, 0, 255)
TEXT_SCALE = 1
TEXT_THICKNESS = 2

# COCO Vehicle Classes
VEHICLE_CLASSES = [2, 3, 5, 7]

CLASS_NAMES = {
    2: "Car",
    3: "Motorcycle",
    5: "Bus",
    7: "Truck"
}
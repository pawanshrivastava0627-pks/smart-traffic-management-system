# ==========================================
# Smart Traffic Management System
# Configuration File
# ==========================================

# Video
VIDEO_PATH = "input/traffic.mp4"

# YOLO Model
MODEL_NAME = "yolov8n.pt"

# Minimum confidence
MIN_CONFIDENCE = 0.40

# Counting Line
LINE_Y = 400
LINE_COLOR = (0, 255, 0)
LINE_THICKNESS = 3

# COCO Vehicle Classes
VEHICLE_CLASSES = [2, 3, 5, 7]

CLASS_NAMES = {
    2: "Car",
    3: "Motorcycle",
    5: "Bus",
    7: "Truck"
}

# Bounding Box Colors (BGR)
CLASS_COLORS = {
    2: (0, 255, 0),      # Car
    3: (0, 255, 255),    # Motorcycle
    5: (255, 0, 0),      # Bus
    7: (0, 0, 255)       # Truck
}
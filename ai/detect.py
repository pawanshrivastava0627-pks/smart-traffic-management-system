from ultralytics import YOLO
import cv2

from config import VIDEO_PATH, MODEL_NAME
from counter import VehicleCounter
from visualizer import draw_counting_line, draw_vehicle_count


def main():

    # Load YOLO model
    model = YOLO(MODEL_NAME)

    # Initialize Counter
    counter = VehicleCounter()

    # Open Video
    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    print("Video loaded successfully!")

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Object Detection + Tracking
        results = model.track(
            frame,
            persist=True,
            verbose=False
        )

        boxes = results[0].boxes

        # Vehicle Counting
        if boxes.id is not None:

            track_ids = boxes.id.int().cpu().tolist()

            for box, track_id in zip(boxes.xyxy, track_ids):

                x1, y1, x2, y2 = box

                center_y = int((y1 + y2) / 2)

                counter.should_count(track_id, center_y)

        # Draw Detection Boxes
        annotated_frame = results[0].plot()

        # Draw UI
        draw_counting_line(annotated_frame)
        draw_vehicle_count(annotated_frame, counter.count)

        # Display Window
        cv2.imshow(
            "Smart Traffic Management System",
            annotated_frame
        )

        # Exit
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
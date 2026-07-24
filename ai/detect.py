from ultralytics import YOLO
import cv2

from config import (
    VIDEO_PATH,
    MODEL_NAME,
    MIN_CONFIDENCE,
    VEHICLE_CLASSES,
    CLASS_NAMES,
    CLASS_COLORS
)

from counter import VehicleCounter
from visualizer import (
    draw_counting_line,
    draw_vehicle_count
)


def main():

    # Load YOLO Model
    model = YOLO(MODEL_NAME)

    # Vehicle Counter
    counter = VehicleCounter()

    # Load Video
    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print("Unable to open video.")
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
            tracker="bytetrack.yaml",
            verbose=False
        )

        annotated_frame = frame.copy()

        boxes = results[0].boxes

        if boxes is not None and boxes.id is not None:

            track_ids = boxes.id.int().cpu().tolist()
            class_ids = boxes.cls.int().cpu().tolist()
            confidences = boxes.conf.cpu().tolist()

            for box, track_id, class_id, conf in zip(
                boxes.xyxy,
                track_ids,
                class_ids,
                confidences
            ):

                # Ignore non-vehicles
                if class_id not in VEHICLE_CLASSES:
                    continue

                # Ignore weak detections
                if conf < MIN_CONFIDENCE:
                    continue

                x1, y1, x2, y2 = map(int, box)

                center_y = int((y1 + y2) / 2)

                # Vehicle Counting
                counter.should_count(
                    track_id,
                    class_id,
                    center_y
                )

                color = CLASS_COLORS[class_id]

                # Bounding Box
                cv2.rectangle(
                    annotated_frame,
                    (x1, y1),
                    (x2, y2),
                    color,
                    2
                )

                # Label
                label = (
                    f"{CLASS_NAMES[class_id]} "
                    f"#{track_id} "
                    f"{conf:.2f}"
                )

                cv2.putText(
                    annotated_frame,
                    label,
                    (x1, max(20, y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    color,
                    2
                )

        # Draw UI
        draw_counting_line(annotated_frame)
        draw_vehicle_count(
            annotated_frame,
            counter
        )

        cv2.imshow(
            "Smart Traffic Management System",
            annotated_frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
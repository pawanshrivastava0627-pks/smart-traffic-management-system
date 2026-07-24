import cv2

from config import (
    LINE_Y,
    LINE_COLOR,
    LINE_THICKNESS
)


def draw_counting_line(frame):
    """
    Draw counting line dynamically according to frame width.
    """

    height, width = frame.shape[:2]

    cv2.line(
        frame,
        (0, LINE_Y),
        (width, LINE_Y),
        LINE_COLOR,
        LINE_THICKNESS
    )


def draw_vehicle_count(frame, counter):
    """
    Display vehicle-wise count.
    """

    colors = {
        "Car": (0, 255, 0),
        "Motorcycle": (0, 255, 255),
        "Bus": (255, 0, 0),
        "Truck": (0, 0, 255)
    }

    y = 35

    for vehicle, count in counter.vehicle_counts.items():

        cv2.putText(
            frame,
            f"{vehicle}: {count}",
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            colors[vehicle],
            2
        )

        y += 35

    cv2.line(
        frame,
        (20, y),
        (220, y),
        (255, 255, 255),
        1
    )

    y += 30

    cv2.putText(
        frame,
        f"Total: {counter.total_count}",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )
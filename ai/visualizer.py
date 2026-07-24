import cv2

from config import *


def draw_counting_line(frame):

    cv2.line(
        frame,
        (0, LINE_Y),
        (1280, LINE_Y),
        LINE_COLOR,
        LINE_THICKNESS
    )


def draw_vehicle_count(frame, count):

    cv2.putText(
        frame,
        f"Total Vehicles: {count}",
        TEXT_POSITION,
        cv2.FONT_HERSHEY_SIMPLEX,
        TEXT_SCALE,
        TEXT_COLOR,
        TEXT_THICKNESS
    )
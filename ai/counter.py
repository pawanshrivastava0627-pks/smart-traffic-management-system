from config import LINE_Y, CLASS_NAMES


class VehicleCounter:

    def __init__(self):

        self.counted_ids = set()

        self.previous_positions = {}

        self.vehicle_counts = {
            "Car": 0,
            "Motorcycle": 0,
            "Bus": 0,
            "Truck": 0
        }

    def should_count(self, track_id, class_id, center_y):

        previous_y = self.previous_positions.get(track_id)

        self.previous_positions[track_id] = center_y

        if previous_y is None:
            return

        crossed = previous_y < LINE_Y <= center_y

        if crossed and track_id not in self.counted_ids:

            self.counted_ids.add(track_id)

            vehicle_name = CLASS_NAMES[class_id]

            self.vehicle_counts[vehicle_name] += 1

    @property
    def total_count(self):

        return sum(self.vehicle_counts.values())
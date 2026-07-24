from config import LINE_Y


class VehicleCounter:

    def __init__(self):
        self.count = 0
        self.counted_ids = set()

    def should_count(self, track_id, center_y):

        if center_y > LINE_Y:

            if track_id not in self.counted_ids:
                self.count += 1
                self.counted_ids.add(track_id)

        return self.count
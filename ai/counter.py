class VehicleCounter:

    def __init__(self):
        self.count = 0
        self.counted_ids = set()

    def count_vehicle(self, track_id):
        if track_id not in self.counted_ids:
            self.count += 1
            self.counted_ids.add(track_id)

        return self.count


counter = VehicleCounter()

print(counter.count_vehicle(1))
print(counter.count_vehicle(2))
print(counter.count_vehicle(2))
print(counter.count_vehicle(3))
print(counter.count_vehicle(1))
print(counter.count_vehicle(4))
# truck.py
class Truck:
    def __init__(self, truck_id, speed=18):
        self.truck_id = truck_id
        self.speed = speed
        self.mileage = 0
        self.current_address = '4001 South 700 East'  # Hub address
        self.packages = []

    def load_package(self, package):
        self.packages.append(package)

    def deliver_package(self, package, delivery_time):
        package.status = f"Delivered at {delivery_time}"
        self.packages.remove(package)

    def calculate_travel_time(self, distance):
        return distance / self.speed
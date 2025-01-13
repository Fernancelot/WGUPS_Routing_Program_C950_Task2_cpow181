# truck.py

class Truck:
    def __init__(self, truck_id, speed=18, hub_address='4001 South 700 East'):
        """
        Truck object representing a delivery vehicle.
        :param truck_id: Numeric or string identifier
        :param speed: Truck speed in mph
        :param hub_address: Hub address where the truck starts and ends each run
        """
        self.truck_id = truck_id
        self.speed = speed
        self.hub_address = hub_address
        self.current_address = hub_address
        self.mileage = 0.0
        self.packages = []

    def load_package(self, package):
        """
        Load a single package onto the truck.
        """
        self.packages.append(package)

    def deliver_package(self, package, delivery_time):
        """
        Mark a package as delivered and remove it from the truck.
        """
        package.status = f"Delivered at {delivery_time}"
        self.packages.remove(package)

    def calculate_travel_time(self, distance):
        """
        Calculates travel time in hours from distance and speed.
        This is O(1) for complexity.
        """
        return distance / self.speed
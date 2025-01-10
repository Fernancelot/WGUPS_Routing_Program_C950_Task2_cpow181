# nearest_neighbor.py
import datetime
from distance import get_distance


def nearest_neighbor(truck, addresses, distances):
    current_address = truck.current_address
    while truck.packages:
        nearest_package = None
        nearest_distance = float('inf')
        for package in truck.packages:
            distance = get_distance(current_address, package.address, addresses, distances)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_package = package
        if nearest_package:
            truck.deliver_package(nearest_package, datetime.datetime.now().strftime("%H:%M:%S"))
            truck.mileage += nearest_distance
            current_address = nearest_package.address
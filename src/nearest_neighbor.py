# nearest_neighbor.py
import datetime
from distance import get_distance

def nearest_neighbor(truck, addresses, distances, max_distance=140.0):
    """
    Runs a nearest neighbor route for the given truck, prioritizing
    minimal distance from the current location.
    Halts if the truck surpasses the max_distance or runs out of packages.

    Time complexity: O(n^2) in the worst case (for n packages, each step can
    search through the remaining undelivered packages).

    :param truck: Truck object with loaded packages
    :param addresses: List of addresses
    :param distances: 2D list of distances
    :param max_distance: Maximum route distance for each run
    :return: None (modifies truck state in place)
    """

    current_address = truck.current_address

    while truck.packages:
        if truck.mileage >= max_distance:
            # If we exceed the distance cap, we stop delivering.
            break

        # Find the closest package (by distance) from the current address
        nearest_package = None
        nearest_distance = float('inf')

        for package in truck.packages:
            distance_to_pkg = get_distance(current_address, package.address, addresses, distances)
            if distance_to_pkg < nearest_distance:
                nearest_distance = distance_to_pkg
                nearest_package = package

        if nearest_package:
            # Check if we can travel to nearest_package without exceeding max_distance
            if truck.mileage + nearest_distance <= max_distance:
                # Deliver the package
                package_delivery_time = datetime.datetime.now().strftime("%H:%M:%S")
                truck.mileage += nearest_distance
                truck.deliver_package(nearest_package, package_delivery_time)
                current_address = nearest_package.address
            else:
                # If we can't make that trip, stop
                break
        else:
            # No suitable next package found
            break

    # Return to the hub if time/distance allows (optional check)
    return_to_hub_distance = get_distance(current_address, truck.hub_address, addresses, distances)
    if truck.mileage + return_to_hub_distance <= max_distance:
        truck.mileage += return_to_hub_distance
        truck.current_address = truck.hub_address
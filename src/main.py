'''
[ Task 2 : Implementation Phase of the WGUPS Routing Program ]

Christopher D Powell  (Fernancelot)
Student ID 001307071
WGU Email: cpow181@wgu.edu
01/09/2025
C950 Data Structures and Algorithms II - Task 2
Course Version NHP3
Python Version: 3.13.1
IDE: PyCharm 2024.1.4 (Professional Edition)
Build #PY-241.18034.82, built on June 24, 2024
OS: Windows 11
'''

# main.py
import datetime
from load_data import load_addresses, load_distances, load_packages
from hash_table import HashTable
from distance import get_distance
from truck import Truck
from package import Package
from nearest_neighbor import nearest_neighbor

# Load data from CSV files
addresses = load_addresses('data/addresses.csv')
distances = load_distances('data/distance.csv')
packages_data = load_packages('data/packages.csv')

# Initialize hash table and insert packages
hash_table = HashTable()
for package_data in packages_data:
    package = Package(*package_data)
    hash_table.insert(package.package_id, package)

# Initialize trucks
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)

# Load packages into trucks based on package ID
for package_id in range(1, 41):
    package = hash_table.lookup(package_id)
    if package:
        if package_id <= 16:
            truck1.load_package(package)
        elif package_id <= 32:
            truck2.load_package(package)
        else:
            truck3.load_package(package)

# Deliver packages using Nearest Neighbor algorithm
nearest_neighbor(truck1, addresses, distances)
nearest_neighbor(truck2, addresses, distances)
nearest_neighbor(truck3, addresses, distances)

# Example usage to print package status
current_time = datetime.datetime.now().strftime("%H:%M:%S")
package = hash_table.lookup(1)
if package:
    print(f"Package ID: {package.package_id}")
    print(f"Address: {package.address}")
    print(f"City: {package.city}")
    print(f"State: {package.state}")
    print(f"Zip: {package.zip_code}")
    print(f"Delivery Deadline: {package.deadline}")
    print(f"Weight: {package.weight}")
    print(f"Special Notes: {package.notes}")
    print(f"Status at {current_time}: {package.status}")
else:
    print(f"Package ID 1 not found.")
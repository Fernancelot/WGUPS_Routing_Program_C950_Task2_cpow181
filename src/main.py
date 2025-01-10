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
Build #PY-241.18034.82, built on June 24, 2025
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
addresses = load_addresses('../data/addresses.csv')
distances = load_distances('../data/distance.csv')
packages_data = load_packages('../data/packages.csv')

# Initialize hash table and insert packages
hash_table = HashTable()
for package_data in packages_data:
    package = Package(*package_data[:8])
    hash_table.insert(int(package.package_id), package)

# Initialize trucks
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)

# Load packages into trucks based on package ID
for package_id in range(1, 41):
    package = hash_table.lookup(int(package_id))
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

def print_package_status(package_id):
    package = hash_table.lookup(package_id)
    if package:
        print(f"Package ID: {package.package_id}")
        print(f"Address: {package.address}")
        print(f"City: {package.city}")
        print(f"State: {package.state}")
        print(f"Zip: {package.zip_code}")
        print(f"Delivery Deadline: {package.deadline}")
        print(f"Weight: {package.weight}")
        print(f"Special Notes: {package.notes}")
        print(f"Status: {package.status}")
        print(f"Delivery Time: {package.delivery_time}")
    else:
        print(f"Package ID {package_id} not found.")

def print_all_packages_status():
    for package_id in range(1, 41):
        print_package_status(package_id)
        print('-' * 40)

def print_total_mileage():
    total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
    print(f"Total mileage traveled by all trucks: {total_mileage:.2f} miles")

def main():
    while True:
        print("\n WGUPS - Western Governors uNDERGRADUATE Parcel Service")
        print("\nWGUPS Routing Program")
        print("1. Print all package statuses")
        print("2. Get a single package status")
        print("3. Get all package statuses at a specific time")
        print("4. Print total mileage traveled by all trucks")
        print("5. Exit")
        # print("? NEVER Select This Choice !!")

        choice = input("Enter your choice: ")

        if choice == '?':
            print()
        if choice == '1':
            print_all_packages_status()
        elif choice == '2':
            package_id = int(input("Enter package ID: "))
            print_package_status(package_id)
        elif choice == '3':
            time = input("Enter time (HH:MM:SS): ")
            # Implement functionality to get all package statuses at a specific time
        elif choice == '4':
            print_total_mileage()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
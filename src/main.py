# main.py
import os
import datetime
from hash_table import HashTable
from load_data import load_addresses, load_distances, load_packages
from scheduler import schedule_packages, create_trucks_for_run
from nearest_neighbor import nearest_neighbor
from package import Package

def print_all_package_statuses(packages):
    for package in packages:
        print(f"Package ID: {package.package_id}, Status: {package.status}")

def lookup_package_status(packages, package_id, lookup_time):
    for package in packages:
        if package.package_id == package_id:
            print(f"Package ID: {package.package_id}, Status at {lookup_time}: {package.status}")
            return
    print(f"Package ID {package_id} not found.")

def lookup_all_package_statuses(packages, lookup_time):
    for package in packages:
        print(f"Package ID: {package.package_id}, Status at {lookup_time}: {package.status}")

def main():
    # 1) Load data
    addresses = load_addresses('../data/addresses.csv')
    distances = load_distances('../data/distance.csv')
    packages_data = load_packages('../data/packages.csv')

    # 2) Insert all packages into a HashTable
    hash_table = HashTable()
    for data in packages_data:
        package_id = int(data[0])
        hash_table.insert(package_id, data)

    # Convert to Package objects
    all_packages = []
    for i in range(len(packages_data)):
        pkg_data = hash_table.lookup(i + 1)
        if pkg_data:
            p = Package(int(pkg_data[0]),
                        pkg_data[1],
                        pkg_data[2],
                        pkg_data[3],
                        pkg_data[4],
                        pkg_data[5],
                        pkg_data[6],
                        pkg_data[7])
            all_packages.append(p)

    # 3) Schedule packages across multiple runs, considering deadlines
    runs = schedule_packages(all_packages, num_trucks=2, capacity=16)

    grand_total_mileage = 0

    # 4) Execute each run
    for run_index, run_data in enumerate(runs, start=1):
        trucks = create_trucks_for_run(run_data)
        print(f"=== Starting Run {run_index} ===")

        # Each truck uses nearest_neighbor route, constrained to 140 miles
        for truck in trucks:
            nearest_neighbor(truck, addresses, distances, max_distance=140.0)
            print(f"Truck {truck.truck_id} finished run with {truck.mileage:.2f} miles.")
            grand_total_mileage += truck.mileage

        print()

    # 5) Final summary
    print(f"All runs complete. Grand total mileage: {grand_total_mileage:.2f}")

    # User Interface
    while True:
        print("\nMenu:")
        print("1. Print all package statuses and total mileage")
        print("2. Lookup single package status at a specific time")
        print("3. Lookup all package statuses at a specific time")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print_all_package_statuses(all_packages)
            print(f"Total mileage: {grand_total_mileage:.2f}")
        elif choice == '2':
            package_id = int(input("Enter package ID: "))
            lookup_time = input("Enter time (HH:MM:SS): ")
            lookup_package_status(all_packages, package_id, lookup_time)
        elif choice == '3':
            lookup_time = input("Enter time (HH:MM:SS): ")
            lookup_all_package_statuses(all_packages, lookup_time)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
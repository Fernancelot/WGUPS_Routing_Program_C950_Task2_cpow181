import datetime
from load_data import load_addresses, load_distances, load_packages
from hash_table import HashTable
from distance import get_distance

# Load data
addresses = load_addresses('data/addresses.csv')
distances = load_distances('data/distance.csv')
packages = load_packages('data/packages.csv')

# Initialize hash table
hash_table = HashTable()
for package in packages:
    package_id = int(package[0])
    hash_table.insert(package_id, package)

# User interface
def print_package_status(package_id, time):
    package = hash_table.lookup(package_id)
    if package:
        print(f"Package ID: {package[0]}")
        print(f"Address: {package[1]}")
        print(f"City: {package[2]}")
        print(f"State: {package[3]}")
        print(f"Zip: {package[4]}")
        print(f"Delivery Deadline: {package[5]}")
        print(f"Weight: {package[6]}")
        print(f"Special Notes: {package[7]}")
        print(f"Status at {time}: {package[8]}")
    else:
        print(f"Package ID {package_id} not found.")

# Example usage
current_time = datetime.datetime.now().strftime("%H:%M:%S")
print_package_status(1, current_time)
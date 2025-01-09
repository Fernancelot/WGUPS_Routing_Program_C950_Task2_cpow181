import csv

def load_addresses(file_path):
    addresses = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            addresses.append(row)
    return addresses

def load_distances(file_path):
    distances = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            distances.append([float(distance) if distance else 0.0 for distance in row])
    return distances

def load_packages(file_path):
    packages = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            packages.append(row)
    return packages

# Example usage
addresses = load_addresses('data/addresses.csv')
distances = load_distances('data/distance.csv')
packages = load_packages('data/packages.csv')

print(addresses)
print(distances)
print(packages)
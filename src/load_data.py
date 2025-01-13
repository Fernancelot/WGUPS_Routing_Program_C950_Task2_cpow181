# load_data.py
import csv
import os

def load_addresses(file_path):
    addresses = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            addresses.append(row[2])
    return addresses

def load_distances(file_path):
    distances = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            distances.append([float(distance) if distance else 0.0 for distance in row])
    return distances

def load_packages(file_path):
    packages = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            packages.append(row)
    return packages
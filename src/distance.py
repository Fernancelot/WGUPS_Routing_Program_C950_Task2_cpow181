# distance.py

def get_distance(address1, address2, addresses, distances):
    index1 = addresses.index(address1)
    index2 = addresses.index(address2)
    return distances[index1][index2]
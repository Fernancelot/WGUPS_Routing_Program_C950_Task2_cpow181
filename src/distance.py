def get_distance(address1, address2, addresses, distances):
    index1 = addresses.index(address1)
    index2 = addresses.index(address2)
    return distances[index1][index2]

# Example usage - comment out or remove these lines if you're not planning to use them here
# address1 = '195 W Oakland Ave'
# address2 = '2530 S 500 E'
# distance = get_distance(address1, address2, addresses, distances)
# print(f"Distance between {address1} and {address2}: {distance} miles")
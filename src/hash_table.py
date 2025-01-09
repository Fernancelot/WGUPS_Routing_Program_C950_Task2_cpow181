class HashTable:
    def __init__(self, size=40):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))

    def lookup(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

# Example usage
hash_table = HashTable()
for package in packages:
    package_id = int(package[0])
    hash_table.insert(package_id, package)

print(hash_table.lookup(1))  # Lookup package with ID 1
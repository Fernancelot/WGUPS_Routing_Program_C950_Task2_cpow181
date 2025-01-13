# hash_table.py

class HashTable:
    def __init__(self, size=40):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))

    def load_packages(self, packages):
        for package in packages:
            package_id = int(package[0])
            self.insert(package_id, package)

    def lookup(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
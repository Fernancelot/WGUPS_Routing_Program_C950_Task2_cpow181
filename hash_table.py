# hash_table.py
# Author: Christopher Powell
# Student ID: 001307071

class HashTable:
    """Hash table implementation for WGUPS package management.
    Average time complexity: O(1) for insertions and lookups
    Worst case: O(n) when collisions occur"""
    
    def __init__(self, initial_capacity=40):
        """Initialize hash table with given capacity. O(1)"""
        self.table = [[] for _ in range(initial_capacity)]
        self.size = 0
        self.capacity = initial_capacity
        self.LOAD_FACTOR_THRESHOLD = 0.7

    def _hash(self, key):
        """Generate hash value for key. O(1)"""
        return hash(str(key)) % self.capacity

    def insert(self, key, item):
        """Insert item with given key. O(1) average case, O(n) worst case"""
        bucket_index = self._hash(key)
        bucket = self.table[bucket_index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, item)
                return
                
        bucket.append((key, item))
        self.size += 1
        
        if self.size / self.capacity >= self.LOAD_FACTOR_THRESHOLD:
            self._resize()

    def lookup(self, key):
        """Lookup item by key. O(1) average case, O(n) worst case"""
        bucket = self.table[self._hash(key)]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def _resize(self):
        """Double table size when load factor threshold reached. O(n)"""
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def get_all(self):
        """Get all items in hash table. O(n)"""
        all_items = []
        for bucket in self.table:
            all_items.extend([v for k, v in bucket])
        return sorted(all_items, key=lambda x: x.package_id)

    def clear(self):
        """Clear all items from hash table. O(1)"""
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0
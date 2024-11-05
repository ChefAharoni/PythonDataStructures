class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # List of lists for chaining

    def _hash(self, key):
        return hash(key) % self.size  # Simple modulo-based hash function

    def insert(self, key, value):
        index = self._hash(key)
        # Check if the key exists and update
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        # If key does not exist, append new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None  # Key not found

    def remove(self, key):
        index = self._hash(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return True
        return False  # Key not found


# Example usage:
hash_table = HashTable()
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
print(hash_table.get("apple"))  # Output: 1
hash_table.remove("apple")
print(hash_table.get("apple"))  # Output: None

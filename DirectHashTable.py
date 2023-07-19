# Direct access table used since package data is small.
# No collisions and all package ids are positive integers.
# Different (hash) table such as chaining or open addressing will be needed to scale with larger data sets.
class DirectHashTable:

    # space complexity: O(n)
    # constructor
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.current_index = 0  # Used for __iter__

    # time complexity: O(1)
    def insert(self, key, value):
        index = int(key-1)  # Adjust for positive integer package id.
        self.table[index] = value

    # time complexity: O(1)
    def remove(self, key):
        self.table[key-1] = None

    # time complexity: O(1)
    def search(self, key):
        return self.table[key-1]

    # Override method to allow hash table to be iterable.
    def __iter__(self):
        self.current_index = 0  # Reset current_index for each iteration loop.
        return self

    # time complexity: O(n)
    # Override method to iterate through table.
    def __next__(self):
        if self.current_index >= self.size:
            raise StopIteration
        else:
            value = self.table[self.current_index]
            self.current_index += 1
            return value

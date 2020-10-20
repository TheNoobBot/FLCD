from lab2.HashMap import HashMap


class SymbolicTable:

    def __init__(self):
        self.hashmap = HashMap()
        self.size = 0

    def add(self, key):
        self.size += 1
        self.hashmap.set(key, self.size)

    def get(self, key):
        return self.hashmap.get(key)

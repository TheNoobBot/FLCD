from lab2.HashMap import HashMap


# This class is used as a symbolic table for the program
class SymbolicTable:

    def __init__(self):
        self.hashmap = HashMap()
        self.size = 0

    # Adds a token into the symbolic table
    def add(self, token):
        self.size += 1
        self.hashmap.set(token, self.size)

    # Gets a token address from the symbolic table
    # If the token is not in the symbolic table, it will raise an exception
    def get(self, token):
        return self.hashmap.get(token)

    # returns all the keys of the symbolic table
    def keys(self):
        return self.hashmap.keys()

# It is a node of a Linked list, it has a key, value and may have a next node
class Node:

    def __init__(self, key, value, next_node=None):
        self.__key = key
        self.__value = value
        self.__next_node = next_node

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def key(self):
        return self.__key

    @property
    def next(self):
        return self.__next_node

    @next.setter
    def next(self, node):
        self.__next_node = node


# It is a basic HashMap with a linked list implementation so that it has a fixed size and only one hash method
# Each time a value is added, it will hash the key, it will check that position in a list, if there is already a value
# it will hop through the nodes until the last link and it will create a new node at the end
class HashMap:
    DEFAULT_SIZE = 100

    def __init__(self, size=DEFAULT_SIZE):
        self.__size = size
        self.__length = 0
        self.__nodes = [None] * size
        self.__keys = []

    # Hashed a string key into an integer
    def hash(self, key) -> int:
        key_hash_sum = 0
        for position, char in enumerate(key):
            key_hash_sum += (position + 1) * ord(char)
        key_hash = key_hash_sum % self.__size
        # print(f"Hashed key {key} into {key_hash}")
        return key_hash

    # Creates a {key, value} node if the key is not in the HashMap
    # Updates the value if the key already is in the HashMap
    def set(self, key, value=None):
        key_hash: int = self.hash(key)
        node = self.__nodes[key_hash]
        index = 0
        if node is None:
            if value is None:
                value = f"{key_hash}-{index}"
            node = Node(key, value)
            self.__length += 1
            self.__keys.append(key)
            self.__nodes[key_hash] = node
            return
        prev = node
        while node is not None:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next
            index += 1
        self.__length += 1
        self.__keys.append(key)
        if value is None:
            value = f"{key_hash}-{index}"
        prev.next = Node(key, value)

    # Returns the value of the key
    # It hashes the key, gets the first node and goes through the LinkedList until a node with the same
    # unhashed key is found
    def get(self, key):
        key_hash: int = self.hash(key)
        node = self.__nodes[key_hash]
        while node is not None:
            if node.key == key:
                # print(f"For key {key} the value found is: {node.value}")
                return node.value
            node = node.next
        raise Exception("Key not found!")

    # Returns true/false if the key is in the HashMap. It works just like the get
    def contains(self, key):
        key_hash: int = self.hash(key)
        node = self.__nodes[key_hash]
        while node is not None:
            if node.key == key:
                # print(f"For key {key} the value found is: {node.value}")
                return True
            node = node.next
        return False

    # Returns all the unhashed keys of the HashMap
    def keys(self):
        return self.__keys

    def __len__(self):
        return self.__length

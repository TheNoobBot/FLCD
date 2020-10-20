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


class HashMap:
    DEFAULT_SIZE = 100

    def __init__(self, size=DEFAULT_SIZE):
        self.__size = size
        self.__length = 0
        self.__nodes = [None] * size

    def hash(self, key) -> int:
        key_hash_sum = 0
        for position, char in enumerate(key):
            key_hash_sum += (position + 1) * ord(char)
        key_hash = key_hash_sum % self.__size
        print(f"Hashed key {key} into {key_hash}")
        return key_hash

    def set(self, key, value):
        key_hash: int = self.hash(key)

        node = self.__nodes[key_hash]
        if node is None:
            node = Node(key, value)
            self.__length += 1
            self.__nodes[key_hash] = node
            return
        prev = node
        while node is not None:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next
        self.__length += 1
        prev.next = Node(key, value)

    def get(self, key):
        key_hash: int = self.hash(key)
        node = self.__nodes[key_hash]
        while node is not None:
            if node.key == key:
                print(f"For key {key} the value found is: {node.value}")
                return node.value
            node = node.next
        raise Exception("Key not found!")

    def contains(self, key):
        key_hash: int = self.hash(key)
        node = self.__nodes[key_hash]
        while node is not None:
            if node.key == key:
                print(f"For key {key} the value found is: {node.value}")
                return True
            node = node.next
        return False

    def __len__(self):
        return self.__length

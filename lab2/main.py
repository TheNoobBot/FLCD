from lab2.HashMap import HashMap

if __name__ == '__main__':
    hashmap = HashMap()

    hashmap.set("hello", "world")
    hashmap.set("diferit", "diferit")
    hashmap.set("UU", "asflgasfl")
    print(hashmap.get("hello"))
    print(hashmap.get("diferit"))
    print(hashmap.get("UU"))
    print(len(hashmap))
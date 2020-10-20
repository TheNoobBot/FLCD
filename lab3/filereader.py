from lab2.HashMap import HashMap


def read_program(file_path):
    file1 = open(file_path, 'r')
    lines = file1.readlines()
    file1.close()
    return ";".join([line.replace("\n", "").replace("\t", "") for line in lines])


def read_tokens(file_path):
    hashmap = HashMap()
    file1 = open(file_path, 'r')
    lines = file1.readlines()
    file1.close()
    for line in lines:
        key, value = line.replace("\n", "").split(" ")
        hashmap.set(key, value)
    return hashmap
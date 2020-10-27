# This file is reading from files


# It reads all the lines from the file given as parameter
# Deletes every newline and tab character from the file
def read_program(file_path):
    file1 = open(file_path, 'r')
    lines = file1.readlines()
    file1.close()
    return " ".join([line.replace("\n", "").replace("\t", "") for line in lines])


# It will read from the file_path the tokens which are in a specific order, and based on their key, it will add it to
# the correspondig category
#   2 <= separators <= 11
#  12 <= operators <= 18:
# The rest are keywords
def read_tokens(file_path):
    separators = []
    operators = []
    keywords = []
    file1 = open(file_path, 'r')
    lines = file1.readlines()
    file1.close()
    for line in lines:
        value, index = line.replace("\n", "").split(" ")
        index = int(index)
        if 2 <= index <= 11:
            separators.append(value)
        elif 12 <= index <= 18:
            operators.append(value)
        else:
            keywords.append(value)
    return operators, separators, keywords

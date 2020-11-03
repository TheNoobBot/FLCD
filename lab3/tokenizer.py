from lab3.filereader import read_program
import re


# This is the main tokenizer, it takes the file name and it will convert it in tokens based on the separators
# First it will read the data from the file, than it will remove the comments from it and it will split it into tokens
def tokenize(input_file, separators):
    full_program = read_program(input_file)
    program = remove_comments(full_program)
    return split_tokens(program, separators)


# It takes as argument the whole program and removes the comments from it
# Reason: The comments are only helpful for the programmer, not for the scanner
def remove_comments(full_program):
    filtered = ""
    comment_found = False
    string_started = False
    for char in full_program:
        if char == "\"":
            string_started = not string_started
            filtered += char
        elif char == "~" and not string_started:
            comment_found = not comment_found
        elif not comment_found:
            filtered += char
    return filtered


# It will take as argument the whole program and it will replace every string/char with a string notation ( ${id}$ )
# It is usefull because later on when split into tokens the ${id}$ it will be considered as 1 token
def separate_strings(program):
    strings = []
    separated = ""
    string = ""
    string_started = False
    index = 0
    for char in program:
        if char == "\"" or char == "\'":
            if not string_started:
                string = f"{char}"
                string_started = True
            else:
                string += f"{char}"
                strings.append(string)
                string_started = False
                separated += f"${index}$"
                index += 1

        elif string_started:
            string += char
        else:
            separated += char
    return separated, strings


# Has 2 parameters. The whole program and the separator
# First it will separate the strings with the program, then it will split into tokens and than it will reunite the
# tokens with the strings where a string/char token is found
def split_tokens(full_program, separators):
    program, strings = separate_strings(full_program)
    for separator in separators:
        program = program.replace(separator, f" {separator} ")
    tokens = program.split(" ")

    for index in range(len(tokens)):
        if re.match("^\$[0-9]+\$$", tokens[index]) is not None:
            string_index = int(tokens[index][1:-1])
            tokens[index] = strings[string_index]

    tokens = [token for token in tokens if token != '']

    with_floats = []
    ignore = 0
    if len(tokens) > 3:
        for token_index in range(0, len(tokens) - 2):
            if ignore == 0:
                together = tokens[token_index] +  tokens[token_index+1] + tokens[token_index+2]
                if float(together):
                    with_floats.append(together)
                    ignore = 2
                else:
                    with_floats.append(tokens[token_index])
            else:
                ignore -= 1
    return with_floats


def float(token):
    return re.match("^0\.[0-9]*$", token) is not None or re.match("^-?[1-9][0-9]*\.[0-9]+$", token) is not None

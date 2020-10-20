from lab3.filereader import read_program, read_tokens


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


def remove_double_separator(full_program):
    string_started = False
    separator_found = False
    program = ""
    for char in full_program:
        if char == "\"":
            string_started = not string_started
            program += char
            separator_found = False
        elif (char == ";" or char == " ") and separator_found and not string_started:
            continue
        else:
            program += char
            separator_found = False

    while ";;" in program:
        program = program.replace(";;", ";")

    return program


def separate_strings(program):
    strings = []
    separated = ""
    string = ""
    string_started = False
    for char in program:
        if char == "\"":
            if not string_started:
                string = ""
                string_started = True
            else:
                strings.append(string)
                string_started = False
                separated += "$"

        elif string_started:
            string += char
        else:
            separated += char
    return separated, strings


def spacing(program):
    return program.replace(";", " ; ").replace("(", " ( ").replace(")", " ) ")


def split_tokens(full_program):
    string_started = False
    token = ""

    program, strings = separate_strings(spacing(full_program))
    tokens = program.split(" ")
    tokens.remove('')
    print("pass")


def tokenize(input_file, token_file):
    tokens = read_tokens(token_file)
    full_program = read_program(input_file)
    program = remove_double_separator(remove_comments(full_program))
    print(program.replace(";", "\n"))
    split_tokens(program)
    print("pass")


if __name__ == '__main__':
    tokenize("inputs/p1.in", "inputs/token.in")

from lab3.SymbolicTable import SymbolicTable
from lab3.filereader import read_tokens
from lab3.tokenizer import tokenize
import re


class Scanner:

    def __init__(self, token_file="inputs/token.in"):
        self.operators, self.separators, self.keywords = read_tokens(token_file)
        self.tokens = self.operators + self.separators + self.keywords
        self.pif = []
        self.symbolicTable = SymbolicTable()

    # reads tokenizes the file content after which classifies and codifies them, then prints the result in output files
    def scan(self, file):
        contains_error = False
        tokens = tokenize(file, self.separators)
        self.pif = []
        self.symbolicTable = SymbolicTable()
        for token in tokens:
            codification = self.classify(token)
            if codification is None:
                self.pif.append((
                    f"Codification error. Invalid token {token} at line {self.get_token_first_location(file, token)}",
                    -1,))
                contains_error = True
            else:
                self.codify(token, codification)
        if contains_error:
            print(f"There is a lexycal in {file} error. Please check the {file[7:-3]}.pif for more info")
        else:
            print(f"{file} success!")

        file = file.split("/")[-1]
        with open(f"outputs/{file[:-3]}.pif", 'w') as out_file:
            out_file.write(f"TokenId  ->  Address(or -1)\n")
            for pif in self.pif:
                out_file.write(f"{pif[0]}  ->  {pif[1]}\n")
        with open(f"outputs/{file[:-3]}.st", 'w') as out_file:
            out_file.write(f"Address  ->  Value\n")
            for key in self.symbolicTable.keys():
                out_file.write(f"{self.symbolicTable.get(key)}  ->  {key}\n")
        with open(f"outputs/{file[:-3]}.out", 'w') as out_file:
            separated = False
            for token in tokens:
                if token in self.separators:
                    separated = True
                    out_file.write(f"{token}")
                elif separated:
                    out_file.write(f"{token}")
                    separated = False
                else:
                    out_file.write(f" {token}")
                if token == ";" or token == ":":
                    out_file.write("\n")

    # Returns the class type of the token
    # -1 if it is a predefined token
    # 0 if identifier
    # 1 if constant
    # None otherwise
    def classify(self, token):
        if token in self.tokens:
            return -1
        elif self.identifier(token):
            return 0
        elif self.constant(token):
            return 1
        else:
            return None

    # It will take a token and it's clasification and based on it, it will add it to the pif or symbolicTable
    # -1 (predefined token) - PIF as {token}, -1
    # 0 or 1 (identifier or constant) - PIF as {token}, {key}
    def codify(self, token, classification):
        if classification == -1:
            self.pif.append((self.tokens.index(token), -1,))

        elif classification == 0 or classification == 1:
            try:
                key = self.symbolicTable.get(token)
                self.pif.append((classification, key,))
            except Exception:
                self.symbolicTable.add(token)
                key = self.symbolicTable.get(token)
                self.pif.append((classification, key,))

    # checks whether the token is of format ^[A-z][0-9A-z]*$
    @staticmethod
    def identifier(token):
        return re.match("^[A-z][0-9A-z]*$", token) is not None

    # checks whether the token is of format ^[1-9][0-9]*$ or 0
    @staticmethod
    def int(token):
        return token == "0" or re.match("^-?[1-9][0-9]*$", token) is not None

    @staticmethod
    # checks whether the token is of format ^0\.[0-9]*$ or ^-?[1-9][0-9]*\.[0-9]+$
    def float(token):
        return re.match("^0\.[0-9]*$", token) is not None or re.match("^-?[1-9][0-9]*\.[0-9]+$", token) is not None

    # checks whether the token is of format ^\'.\'$
    @staticmethod
    def char(token):
        return re.match("^\'.\'$", token) is not None

    # checks whether the token is of format ^\".*\"$
    @staticmethod
    def string(token):
        return re.match("^\".*\"$", token) is not None

    # checks whether the token is true of false
    @staticmethod
    def bool(token):
        return token == "true" or token == "false"

    # checks whether the token is int, char, string or bool
    def constant(self, token):
        return self.int(token) or self.float(token) or self.char(token) or self.string(token) or self.bool(token)

    # Returns the location of the token in a file.
    # It is used so we will know when an invalid token is found the line where it is
    @staticmethod
    def get_token_first_location(file, token):
        commented = False
        with open(file) as myFile:
            for num, line in enumerate(myFile, 1):
                if line.count("~") % 2 == 1:
                    commented = not commented
                elif token in line and commented is False:
                    return num

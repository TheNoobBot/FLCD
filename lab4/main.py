# input definition
# first line the states with spaces between them
# second line the alphabet with spaces between elements
# third line the initial state
# fourth line the final states with spaces betweem them
# next len(alphabet) lines the transitions in "state element state" format


class FA:
    def __init__(self, file_path):
        file_program = self.read_program(file_path)
        self.states = file_program[0]
        self.alphabet = file_program[1]
        self.initial = file_program[2][0]
        self.final = file_program[3][0]
        self.transitions = {(state, element,): next_state for state, element, next_state in file_program[4:]}
        self.data = [self.alphabet, self.states, self.transitions, self.initial, self.final]

    def validate_sequence(self, sequence):
        state = self.initial
        while len(sequence) > 0 and state is not None:
            transition = (state, sequence.pop(0))
            state = self.transitions[transition] if transition in self.transitions.keys() else None
        return state is not None and state in self.final

    @staticmethod
    def read_program(file_path):
        file1 = open(file_path, 'r')
        lines = file1.readlines()
        file1.close()
        return [line.replace("\n", "").replace("\t", "").split(" ") for line in lines]

    def read_sequence(self):
        print(self.validate_sequence(input("Please insert a sequence: ").split(" ")))

    def print_data(self, index=-1):
        if index == -1:
            exit()
        else:
            print(self.data[index - 1])


if __name__ == '__main__':
    fa = FA("FA.in")
    print("""
    0 - read_sequence
    1 - print_alphabet
    2 - print_states
    3 - print_transitions
    4 - print_initial
    5 - print_final
    6 - exit
    """)
    menu = {
        "0": fa.read_sequence,
        "1": lambda: fa.print_data(1),
        "2": lambda: fa.print_data(2),
        "3": lambda: fa.print_data(3),
        "4": lambda: fa.print_data(4),
        "5": lambda: fa.print_data(5),
        "6": exit
    }
    while True:
        option = input("Choose an option:")
        if option in menu:
            menu[option]()
        else:
            print("Wrong option")

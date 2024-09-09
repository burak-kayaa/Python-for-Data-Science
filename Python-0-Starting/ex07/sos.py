import sys

def arg_checher(args):
    assert len(args) == 2, "AssertionError: the arguments are bad"
    assert args[1].isalnum(), "AssertionError: the arguments are bad"

def main():
    try:
        arg_checher(sys.argv)
    except AssertionError as e:
        print(e)
        return
    sos(sys.argv[1])

def sos(string):
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }
    for char in string:
        print(NESTED_MORSE[char.upper()], end="")
    print()

if __name__ == '__main__':
    main()
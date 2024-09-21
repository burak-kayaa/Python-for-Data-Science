import sys


def arg_checher(args):
    """
    Check if the arguments are valid
    """
    assert len(args) == 2, "AssertionError: the arguments are bad"
    assert args[1].isalnum(), "AssertionError: the arguments are bad"


def main():
    """
    Main function
    """
    try:
        arg_checher(sys.argv)
        sos(sys.argv[1])
    except AssertionError as e:
        print(e)
        return


def sos(string):
    """
    Print the morse code of a string
    """
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
    assert string in NESTED_MORSE, "AssertionError: the arguments are bad"
    for char in string:
        print(NESTED_MORSE.get(char.upper(), ""), end="")
    print()


if __name__ == '__main__':
    main()

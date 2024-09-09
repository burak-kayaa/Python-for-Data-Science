""" This is a building module """
import sys


def building(str):
    """ This is a building function """
    puncs = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    character_count = len(str)
    upper_letters = [c for c in str if c.isupper()]
    lower_letters = [c for c in str if c.islower()]
    puncp = [c for c in str if c in puncs]
    spaces = [c for c in str if c.isspace()]
    digits = [c for c in str if c.isdigit()]

    print(f"The text contains {character_count} characters:")
    print(f"{len(upper_letters)} upper letters")
    print(f"{len(lower_letters)} lower letters")
    print(f"{len(puncp)} punctuation marks")
    print(f"{len(spaces)} spaces")
    print(f"{len(digits)} digits")


def main():
    """ Main entry point of the app """
    try:
        assert len(sys.argv) <= 2
    except AssertionError:
        print("Usage: python building.py <building_name> | python building.py")
        return 1
    if len(sys.argv) == 2:
        building(sys.argv[1])
    else:
        try:
            input_text = input("What is the text to count?\n")
            building(input_text + "\n")
        except EOFError:
            pass


if __name__ == "__main__":
    main()

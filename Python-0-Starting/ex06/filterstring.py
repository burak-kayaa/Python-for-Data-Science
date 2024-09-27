import sys
from ft_filter import ft_filter


def arg_checker(args):
    """
    Check if the arguments are valid
    """
    puncs = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    not_printables = ft_filter(lambda x: not x.isprintable(), args[1])
    try:
        assert len(args) == 3
        assert args[2].isnumeric()
        puncp = [c for c in args[1] if c in puncs]
        assert len(puncp) == 0
        assert len(not_printables(args[1])) == 0
    except AssertionError:
        print("Usage: python filterstring.py <string> <number>")
        return 1
    return 0


def main():
    """
    Main function
    """
    if arg_checker(sys.argv):
        return 1
    string = sys.argv[1]
    strings = string.split()
    number = int(sys.argv[2])
    filtered = ft_filter(lambda x: len(x) > number, strings)
    print(filtered)


if __name__ == '__main__':
    main()

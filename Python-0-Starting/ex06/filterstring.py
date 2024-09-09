import sys


def arg_checker(args):
    puncs = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    not_printables = lambda s: [c for c in s if not c.isprintable()]
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
    if arg_checker(sys.argv):
        return 1
    string = sys.argv[1]
    strings = split(string)
    mains = []
    for i in strings:
        if len(i) > int(sys.argv[2]):
            mains.append(i)
    print(" ".join(mains))



if __name__ == '__main__':
    main()
import sys

try:
    assert len(sys.argv) == 2, "Usage: python3 whatis.py <number>"
    assert sys.argv[1].isdigit(), "Usage: python3 whatis.py <number>"
except AssertionError as e:
    print(f"Error: {e}")
    sys.exit(1)
number = int(sys.argv[1])

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

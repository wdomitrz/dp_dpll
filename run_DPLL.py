import sys
from base import DPLL, most_common

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Expected exactly one argument - the .cnf file name")
        exit(1)
    DPLL(most_common)(sys.argv[1])

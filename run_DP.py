import sys
from base import DP, least_common

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Expected exactly one argument - the .cnf file name")
        exit(1)
    DP(least_common)(sys.argv[1])

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenArgv = len(sys.argv) - 1
    print("{} argument{}".format(lenArgv,"s" if lenArgv != 1 else ""), end="")
    print("{}".format("." if lenArgv == 0 else ":"))
    for i in range(1, lenArgv + 1):
        print("{}: {}".format(i, sys.argv[i]))

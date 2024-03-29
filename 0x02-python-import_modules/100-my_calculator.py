#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, op, b, operations.get(op, "")(a, b)))

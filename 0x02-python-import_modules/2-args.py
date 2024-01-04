#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_args = sys.argv

    if len(num_args) == 1:
        print("0 arguments.")
    elif len(num_args) == 2:
        print("1 argument:")
    elif len(num_args) > 2:
        print("{} arguments:".format(len(num_args) - 1))

    if len(num_args) > 1:
        for i in range(len(num_args) - 1):
            print("{}: {}".format(i + 1, num_args[i + 1]))

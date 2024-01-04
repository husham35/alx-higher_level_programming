#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_args = sys.argv

    total = 0

    if len(num_args) > 1:
        for i in range(len(num_args) - 1):
            total += int(num_args[i + 1])

    print("{}".format(total))

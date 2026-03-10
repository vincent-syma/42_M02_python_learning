#!/usr/bin/env python3

import sys


def main() -> None:
    """
    Entry point of the Command Quest script.
    Parse and display command-line arguments.
    The function inspects sys.argv to determine how many arguments were
    provided and prints them in the required format for the exercise.
    """
    print("=== Command Quest ===")

    total = len(sys.argv)

    if total == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {total}")

    elif total > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {total - 1}")
        count = 1
        for arg in sys.argv[1:]:
            print(f"Argument {count}: {arg}")
            count += 1
        print(f"Total arguments: {total}")


if __name__ == "__main__":
    main()

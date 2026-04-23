#!/usr/bin/env python3

import sys
import os
import site

# ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

# combinations
BOLD_RED = BOLD + RED
BOLD_GREEN = BOLD + GREEN
BOLD_BLUE = BOLD + BLUE

# Authorized: sys, os, site modules, print()


def main() -> None:
    """Entry point of the program"""

    if sys.prefix != sys.base_prefix:  # == is virtual environment
        print("\nMATRIX STATUS: Welcome to the construct")

        print(f"\nCurrent Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")

        print("\n✅ SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        try:
            packages = site.getsitepackages()
            if packages:
                print("\nPackage installation path:")
                print(packages[0])

        except Exception:
            print("Package path not available.")

        finally:
            print("----------------------------------------------")

    else:
        print("\nMATRIX STATUS: You're still plugged in")

        print(f"\nCurrent Python: {sys.executable}")
        print("Virtual Environment: None detected")

        print(f"\n{BOLD_RED}WARNING:{RESET} You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate   # On Windows")

        print("\nThen run this program again.")
        try:
            packages = site.getsitepackages()
            if packages:
                print("\nPackage installation path:")
                print(packages[0])

        except Exception:
            print("Package path not available.")

        finally:
            print("----------------------------------------------")


if __name__ == "__main__":
    main()

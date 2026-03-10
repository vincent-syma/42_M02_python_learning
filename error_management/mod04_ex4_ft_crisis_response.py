#!/usr/bin/env python3

import sys

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


def secure_extraction(file_name: str) -> None:
    """Recover and display archived data from storage vault."""

    try:
        with open(file_name, "r") as file:
            content: str = file.read()
            print(f"SUCCESS:\tArchive recovered:\n\n"
                  f"{ITALIC}'{content}'{RESET}")

    except FileNotFoundError:
        raise FileNotFoundError("Archive not found in storage matrix")

    except PermissionError:
        raise PermissionError("Security protocols deny access")


def main() -> None:
    """
    Entry point of the ancient_text recovery program.
    """
    print()
    print(f"{BOLD}=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ==={RESET}")
    print()

    files = ["lost_archive.txt", "classified_data.txt", "standard_archive.txt"]
    for file_name in files:
        try:
            print(f"CRISIS ALERT:\tAttempting access to "
                  f"{BLUE}'{file_name}'{RESET}...")
            secure_extraction(file_name)
            print()
            print("STATUS:\t\tNormal operations resumed")
            print()

        except FileNotFoundError as e:
            print(f"{RED}RESPONSE:\t{e}{RESET}", file=sys.stderr)
            print("STATUS:\t\tCrisis handled, system stable")
            print()

        except PermissionError as e:
            print(f"{RED}RESPONSE:\t{e}{RESET}", file=sys.stderr)
            print("STATUS:\t\tCrisis handled, security maintained")
            print()

    print(f"✅ {GREEN}All crisis scenarios handled successfully. "
          f"Archives secure.{RESET}")
    print()
    print("---------------------------------------------")


if __name__ == "__main__":
    main()

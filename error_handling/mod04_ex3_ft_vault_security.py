#!/usr/bin/env python3

import sys

# ANSI
RESET = "\033[0m"
BOLD = "\033[1m"

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

    print(f"Initiating secure vault access... {BLUE}{file_name}{RESET}")

    try:
        with open(file_name, "r") as file:
            print("Vault connection established with failsafe protocols")
            print()
            print(f"{BOLD}SECURE EXTRACTION:{RESET}")
            print()
            content: str = file.read()
            print(content)

    except FileNotFoundError:
        print(f"{RED}ERROR: Storage vault not found.{RESET}", file=sys.stderr)


def secure_preservation(file_name: str) -> None:
    """Create new file and fill it with data."""

    try:
        with open(file_name, "w") as file:
            print(f"{BOLD}SECURE PRESERVATION:{RESET}")
            print()
            entry: str = "[CLASSIFIED] New security protocols archived"
            file.write(entry + "\n")
            print(entry)
            print()
            print("✅ Vault automatically sealed upon completion")

    except OSError as e:
        print(f"{RED}ERROR: Unable to initialize storage unit: "
              f"{e}.{RESET}", file=sys.stderr)


def main() -> None:
    """
    Entry point of the ancient_text recovery program.
    """
    print()
    print(f"{BOLD}=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ==={RESET}")
    print()
    secure_extraction("classified_data.txt")
    print()
    secure_extraction("non_existing.txt")
    print()
    secure_preservation("new.txt")
    print()
    secure_preservation("")
    print()
    print("---------------------------------------------")


if __name__ == "__main__":
    main()

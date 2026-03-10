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


def average(scores: list) -> float:
    """
    Calculates average score.
    """
    players = len(scores)
    average = sum(scores) / players
    return average


def main() -> None:
    """
    Entry point of the score analytics program...
    """
    print()
    print(f"{BOLD_BLUE}=== Player Score Analytics ==={RESET}")
    print()

    argc = len(sys.argv)

    if argc == 1:
        print(f"{YELLOW}No scores provided.")
        print(f"Usage: {RESET}python3 ft_score_analytics.py "
              "<score1> <score2> ... ")
        print()
        return None

    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError as e:
            print(f"{RED}Error: {e}{RESET}")
            print()
    if not scores:
        print(f"{YELLOW}No valid scores to process.{RESET}")
        print()
        return None
    print(f"{BOLD}Scores processed: {RESET}{scores}")
    print()
    players = len(scores)
    print(f"{BOLD}Total players:\t{RESET}{players}")
    print()
    avrg = average(scores)
    print(f"{BOLD}Average score:\t{RESET}{avrg:.1f}")
    max_score = max(scores)
    print(f"{BOLD}High score:\t{RESET}{max_score}")
    min_score = min(scores)
    print(f"{BOLD}Low score:\t{RESET}{min_score}")
    print(f"{BOLD}Score range:\t{RESET}{max_score - min_score}")
    print()
    print("-------------------------------")
    print()


if __name__ == "__main__":
    main()

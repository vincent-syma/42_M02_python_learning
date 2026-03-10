#!/usr/bin/env python3

from typing import Generator

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


def game_events(n: int) -> Generator[dict, None, None]:
    """
    Generates "random" event stream.
    """
    players = ["alice", "bob", "charlie", "diana"]
    # event_types = ["kill", "treasure", "level_up"]
    event_types = ["killed monster", "found treasure", "leveled up"]

    for i in range(n):
        event = {
            "id": i + 1,
            "player": players[i % len(players)],
            "event_type": event_types[i % len(event_types)],
            "level": (i % 50) + 1,
        }

        yield event


def fibonacci(n: int) -> Generator[int, None, None]:
    """
    Generates Fibonacci sequence of n numbers as a stream.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime(n: int) -> Generator[int, None, None]:
    """
    Generates the first n prime numbers as a stream.
    """
    count = 0
    a = 2
    while count < n:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                break
        else:
            yield a
            count += 1
        a += 1


def main() -> None:
    """
    Entry point of data stream program.
    """
    print()
    print(f"{BLUE}{BOLD}=== Game Data Stream Processor ==={RESET}")
    print()

    n = 100
    total = 0
    high_level = 0
    treasures = 0
    levelups = 0

    print(f"Processing {n} game events...")

    for event in game_events(n):

        total += 1
        print(f"Event {event['id']}: "
              f"Player {event['player']} "
              f"(level {event['level']}) "
              f"{event['event_type']}")

        if event['level'] >= 10:
            high_level += 1

        if event['event_type'] == "found treasure":
            treasures += 1

        if event['event_type'] == "leveled up":
            levelups += 1

    print()
    print(f"{BOLD}=== Stream Analytics ==={RESET}")
    print()
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {levelups}")

    # print(f"Memory usage: Constant (streaming)")
    # print(f"Processing time: {x} seconds")

    print()
    print(f"{BOLD}=== Generator Demonstration ==={RESET}")
    print()

    n = 10
    print(f"Fibonacci sequence (first {n}):", end=" ")
    first = True
    for num in fibonacci(n):
        if not first:
            print(", ", end="")
        print(f"{num}", end="")
        first = False
    print()

    n = 5
    print(f"Prime numbers (first {n}):", end=" ")
    first = True
    for num in prime(n):
        if not first:
            print(", ", end="")
        print(f"{num}", end="")
        first = False
    print()

    print()


if __name__ == "__main__":
    main()

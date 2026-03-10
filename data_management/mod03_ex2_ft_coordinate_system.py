#!/usr/bin/env python3

import math

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


def create_position(x: int, y: int, z: int) -> tuple:
    """
    Creates tuple position from individual int coordinates.
    """
    pos = (x, y, z)
    return pos


def calculate_distance(position_1: tuple[int, int, int],
                       position_2: tuple[int, int, int]) -> float:
    """
    Calculates distance between 2 3D positions defined by tuples.
    """
    x1, y1, z1 = position_1
    x2, y2, z2 = position_2

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance


def parse_coordinate_string(coordinates: str) -> tuple:
    """
    Parses a string into tuple of ints/coordinates, if valid.
    """
    try:
        parts = coordinates.split(",")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        pos = (x, y, z)

        return pos

    except (ValueError, IndexError) as e:
        raise ValueError(f"Invalid coordinates: {coordinates}") from e


def main() -> None:
    """
    Entry point of the coordinate system program.
    """
    print()
    print(f"{BOLD_BLUE}=== Game Coordinate System ==={RESET}")
    print()

    # Create position
    pos = create_position(10, 20, 5)
    print(f"Position created: {pos}")

    # Distance from zero
    zero = (0, 0, 0)
    distance = calculate_distance(zero, pos)
    print(f"Distance between {zero} and {pos}: {distance:.2f}")

    print()

    # Parsing valid coordinates from str
    good_str = "3,4,0"
    print(f'Parsing coordinates: "{good_str}"')
    try:
        pos_val = parse_coordinate_string(good_str)
        print(f"Parsed position: {pos_val}")
        distance = calculate_distance(zero, pos_val)
        print(f"Distance between {zero} and {pos_val}: {distance:.2f}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        print(f"{YELLOW}Cause: {e.__cause__}{RESET}")

    print()

    # Parsing invalid coordinates from str
    bad_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{bad_str}"')
    try:
        parse_coordinate_string(bad_str)
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        print(f"{YELLOW}Cause: {e.__cause__}{RESET}")
    print()

    # Unpacking demonstration
    if pos_val is not None:
        print("Unpacking demonstration:")
        print(f"Player at:\tx={pos_val[0]}, y={pos_val[1]}, z={pos_val[2]}")
        x, y, z = pos_val
        print(f"Coordinates:\tX={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from .CreatureCard import CreatureCard

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


# --- demonstration script for ex0 ---

def main() -> None:
    """
    Entry point of the demonstration script.
    """

    print(f"\n{BOLD}=== DataDeck Card Foundation ==={RESET}")

    try:
        fire_dragon = CreatureCard("Fire Dragon with 0 attack",
                                   5, "Legendary", 0, 5)
    except ValueError as e:
        print(f"\n{RED}{e}{RESET}")

    try:
        fire_dragon = CreatureCard("Fire Dragon with -1 health",
                                   5, "Legendary", 7, -1)
    except ValueError as e:
        print(f"\n{RED}{e}{RESET}")

    try:
        fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        game_state = {}
        available_mana = 6

        print(f"\n{ITALIC}Testing Abstract Base Class Design:{RESET}")

        print("\nCreatureCard Info:")
        print(fire_dragon.get_card_info())

        print(f"\nPlaying Fire Dragon with {available_mana} mana available:")
        print(f"Playable: {fire_dragon.is_playable(available_mana)}")
        print(f"Play result: {fire_dragon.play(game_state)}")
        available_mana -= fire_dragon.cost

        print("\nFire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {fire_dragon.attack_target("Goblin Warrior")}")

        print(f"\nTesting insufficient mana ({available_mana} available):")
        print(f"Playable: {fire_dragon.is_playable(available_mana)}")

        print("\n✅ Abstract pattern successfully demonstrated!")

    except ValueError as e:
        print(f"\n{RED}{e}{RESET}")

    finally:
        print("-----------------------------------------------------")


if __name__ == "__main__":
    main()

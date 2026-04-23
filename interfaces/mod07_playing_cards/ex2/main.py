#!/usr/bin/env python3

from .EliteCard import EliteCard

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


# --- demonstration script for ex2 ---

def main() -> None:
    """
    Entry point of the demonstration script.
    """

    print(f"\n{BOLD}=== DataDeck Ability System ==={RESET}")

    print("\nEliteCard capabilities:\n")
    for base in EliteCard.__bases__:
        methods = [name for name in dir(base)
                   if callable(getattr(base, name))
                   and not name.startswith("__")]

        print(f"- {base.__name__}: {methods}")

    print(f"\n{ITALIC}>>> Playing Arcane Warrior (Elite Card) <<<{RESET}")
    arcane_warrior = EliteCard("Arcane Warrior", 5, "Rare", 5, 10, 10)

    print("\nCombat phase:\n")
    print(f"Attack result: {arcane_warrior.attack("Enemy")}")
    print(f"Defense result: {arcane_warrior.defend(7)}")

    print("\nMagic phase:\n")
    print(f"Spell cast: {arcane_warrior.cast_spell("Fireball",
                                                   ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")

    print("\n✅ Multiple interface implementation successful!")

    print("-----------------------------------------------------")


if __name__ == "__main__":
    main()

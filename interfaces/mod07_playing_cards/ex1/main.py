#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck

from tools.card_generator import CardGenerator

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


# --- demonstration script for ex1 ---

def main() -> None:
    """
    Entry point of the demonstration script.
    """

    print(f"\n{BOLD}=== DataDeck Deck Builder ==={RESET}")

    print(f"\n{ITALIC}Building deck with different card types...{RESET}\n")

    deck = Deck()
    generator = CardGenerator()
    game_state = {}

    creature = CreatureCard(**generator.get_creature("Fire Dragon"))
    spell = SpellCard(**generator.get_spell("Lightning Bolt"))
    artifact = ArtifactCard(**generator.get_artifact("Mana Crystal"))

    cards = [creature, spell, artifact]

    for card in cards:
        deck.add_card(card)

    print(f"Deck stats:\t{deck.get_deck_stats()}")

    print("\nDECK:\t\t", end="")
    first = True
    for card in deck.cards:
        if not first:
            print(", ", end="")
        first = False
        print(f"{card.name}", end="")

    deck.shuffle()

    print("\nSHUFFLED DECK:\t", end="")
    first = True
    for card in deck.cards:
        if not first:
            print(", ", end="")
        first = False
        print(f"{card.name}", end="")

    print(f"\n\n{ITALIC}Drawing and playing cards:{RESET}")

    while deck.cards:
        card = deck.draw_card()
        print(f"\nDrew:\t\t{card.name} ({card.type})")
        print(f"Play result:\t{card.play(game_state)}")

    print("\n✅ Polymorphism in action: "
          "Same interface, different card behaviors!")

    print("-----------------------------------------------------")


if __name__ == "__main__":
    main()

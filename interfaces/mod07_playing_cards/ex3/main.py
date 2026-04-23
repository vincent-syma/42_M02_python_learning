#!/usr/bin/env python3

from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine

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


# --- demonstration script for ex3 ---

def main() -> None:
    """
    Entry point of the demonstration script.
    """

    print(f"\n{BOLD}=== DataDeck Game Engine ==={RESET}")

    print("\n>>> Configuring Fantasy Card Game... <<<\n")

    game_engine = GameEngine()
    game_engine.configure_engine(FantasyCardFactory(CardGenerator),
                                 AggressiveStrategy)

    print(f"Factory: {type(game_engine.factory).__name__}")
    print(f"Strategy: {game_engine.strategy.__class__.__name__}")
    print()

    try:
        dragon = game_engine.factory.create_creature("dragon")
        print(dragon.get_card_info())

    except ValueError as e:
        print(f"{RED}Error: {e}{RESET}")

    game_engine.factory.create_themed_deck(6)
    print("\nAvailable card types in deck:")
    print(game_engine.factory.get_supported_types())

    print("\nSimulating aggressive turn...\n")
    turn = game_engine.simulate_turn()

    hand = [card.name for card in game_engine.hand]
    print(f"Hand: {hand}")

    print("\nTurn execution:")
    print(f"Strategy: {game_engine.strategy.get_strategy_name()}")
    print(f"Actions: {turn}")

    print("\nGame Report:")
    print(game_engine.get_engine_status())

    print("\n✅ Abstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")

    print("-----------------------------------------------------")


if __name__ == "__main__":
    main()

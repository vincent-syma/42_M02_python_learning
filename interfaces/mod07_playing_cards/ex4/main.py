#!/usr/bin/env python3

from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard
# from tools.card_generator import CardGenerator

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


# --- demonstration script for ex4 ---

def main() -> None:
    """
    Entry point of the demonstration script.
    """

    print(f"\n{BOLD}=== DataDeck Tournament Platform ==={RESET}")

    tournament = TournamentPlatform()

    print("\n>>> Registering Tournament Cards... <<<")

    # generator = CardGenerator()

    # fire_dragon = TournamentCard(**generator.get_creature("Fire Dragon"))
    fire_dragon = TournamentCard(**{"name": "Fire Dragon",
                                    "cost": 5,
                                    "rarity": "Legendary",
                                    "attack_power": 7,
                                    "health": 5})

    # ice_wizard = TournamentCard(**generator.get_creature("Ice Wizard"))
    ice_wizard = TournamentCard(**{"name": "Ice Wizard",
                                   "cost": 4,
                                   "rarity": "Rare",
                                   "attack_power": 3,
                                   "health": 4})

    cards = [fire_dragon, ice_wizard]
    tournament_participants = {}

    for card in cards:
        card_id = tournament.register_card(card)
        tournament_participants.update({card_id: card})

        print(f"\n{card.name} (ID: {card_id}):")

        print(f"- Interfaces: {card.get_card_info()['interfaces']}")

        for key, value in card.get_rank_info().items():
            print(f"- {key.capitalize()}: {value}")

        for key, value in card.get_tournament_stats().items():
            print(f"- {key.capitalize()}: {value}")

    print("\n>>> Creating tournament match... <<<")

    fire_dragon_id = next(k for k, v in tournament_participants.items()
                          if v is fire_dragon)
    ice_wizard_id = next(k for k, v in tournament_participants.items()
                         if v is ice_wizard)

    match = tournament.create_match(fire_dragon_id, ice_wizard_id)
    print(f"Match result: {match}")

    print("\n>>> Tournament Leaderboard: <<<")
    leaderboard = tournament.get_leaderboard()
    count = 1
    for card in leaderboard:
        print(f"{count}. {card.name} - Rating: {card.calculate_rating()} "
              f"({card.get_tournament_stats()['record']})")
        count += 1

    print("\n>>> Platform Report: <<<")

    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("\n✅ All abstract patterns working together harmoniously!")

    print("-----------------------------------------------------")


if __name__ == "__main__":
    main()

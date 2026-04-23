from ex0.Card import Card
import random


class Deck:
    """Deck management class"""

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        """Adds card to the Deck"""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Removes card from the Deck"""
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                del self.cards[i]
                return True
        return False

    def shuffle(self) -> None:
        """Randomizes the order of cards in the Deck"""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Takes the first card from the Deck and removes it from it"""  # ???
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        """Return all available info about the Deck."""

        card_infos = [card.get_card_info() for card in self.cards]

        total_cards = len(self.cards)
        creatures = sum(1 for card in card_infos if card['type'] == "Creature")
        spells = sum(1 for card in card_infos if card['type'] == "Spell")
        artifacts = sum(1 for card in card_infos if card['type'] == "Artifact")
        avg_cost = (sum(card['cost'] for card in card_infos)
                    / total_cards if total_cards else 0)

        return {
            'total_cards': total_cards,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': round(avg_cost, 2)
        }

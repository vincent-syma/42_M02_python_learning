from abc import ABC, abstractmethod


class Card(ABC):
    """Universal card blueprint"""

    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Updates the game state with playing this Card."""
        game_state.update({
            'card played': self.name,
            'mana_used': self.cost
        })
        return game_state

    def get_card_info(self) -> dict:
        """Return all available info about the Card."""
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if player has enough mana to play the card."""

        if available_mana >= self.cost:
            return True
        else:
            return False

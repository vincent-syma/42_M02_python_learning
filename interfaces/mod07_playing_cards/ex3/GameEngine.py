from .GameStrategy import GameStrategy
from .CardFactory import CardFactory


class GameEngine:
    """Game Orchestrator"""

    def __init__(self) -> None:
        self.turns_simulated = 0
        self.total_damage = 0
        self.hand = []
        self.cards_drawn = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Assigns chosen card factory and game strategy
        to this particular game"""
        self.factory = factory
        self.strategy = strategy()

    def simulate_turn(self) -> dict:
        """
        Draws 3 cards from deck to a hand.
        Sends 'hand' and simulated 'battlefield' to the strategy used
        and runs 'execute turn' method.
        """
        self.turns_simulated += 1

        # self.hand = self.factory.create_themed_deck(3)

        for _ in range(3):
            self.hand.append(self.factory.deck.draw_card())
            self.cards_drawn += 1

        battlefield = [
            "Tree",
            "Enemy Player",
            "Friendly creature",
            "Enemy Creature"
        ]

        turn = self.strategy.execute_turn(self.hand, battlefield)
        self.total_damage += turn['damage_dealt']

        return turn

    def get_engine_status(self) -> dict:
        """Returns game stats."""

        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.factory.cards_created,
            'cards_drawn': self.cards_drawn
        }

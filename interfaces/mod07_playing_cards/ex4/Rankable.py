from abc import ABC, abstractmethod


class Rankable (ABC):
    """Abstract ranking interface"""

    def __init__(self):
        self.wins = 0
        self.losses = 0

    @abstractmethod
    def calculate_rating(self) -> int:
        return (1000 + 16 * self.wins - 16 * self.losses)

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        self.wins += wins

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        self.losses += losses

    @abstractmethod
    def get_rank_info(self) -> dict:
        return {
            'rating': self.calculate_rating(),
        }

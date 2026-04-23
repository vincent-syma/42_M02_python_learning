from abc import ABC, abstractmethod


class Combatable (ABC):
    """Abstract combat interface."""

    def __init__(self, attack_power: int, health: int):
        self.attack_power = attack_power
        self.health = health

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass

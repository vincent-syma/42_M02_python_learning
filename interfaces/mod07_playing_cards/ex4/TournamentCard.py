from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard (Card, Combatable, Rankable):
    """Card with tournament capabilities"""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, health: int):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack_power, health)
        Rankable.__init__(self)
        self.type = "Tournament"

    # Card Interface:

    def play(self, game_state: dict) -> dict:
        game_state.update(super().play(game_state))
        game_state.update({
            'effect': 'Card summoned to the battlefield'
        })
        return game_state

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            'type': self.type,
            'attack': self.attack_power,
            'health': self.health,
            'interfaces': [base.__name__ for base in TournamentCard.__bases__]
        })
        return info

    # Rankable Interface:

    def calculate_rating(self) -> int:
        rating = super().calculate_rating()
        rating += 30 * self.attack_power + 30 * self.health
        return rating

    def update_wins(self, wins: int) -> None:
        super().update_wins(wins)

    def update_losses(self, losses: int) -> None:
        super().update_losses(losses)

    def get_rank_info(self) -> dict:
        info = super().get_rank_info()
        return info

    def get_tournament_stats(self) -> dict:
        return {
            'record': f"{self.wins}-{self.losses}",
        }

    # Combatable Interface:

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(incoming_damage - self.attack_power, 0)
        damage_blocked = (
            self.attack_power if incoming_damage > self.attack_power else 0
            )
        self.health -= damage_taken
        still_alive = True if self.health > 0 else False

        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': still_alive
            }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_power,
            'health': self.health,
            'combat_type': "melee",
        }

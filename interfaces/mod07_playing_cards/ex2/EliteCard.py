from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard (Card, Combatable, Magical):
    """
    Multiple inheritance class.
    • Represents powerful cards with multiple abilities
    • Combines combat prowess with magical capabilities
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, health: int, mana: int):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack_power, health)
        Magical.__init__(self, mana)
        self.type = "Elite"

    def play(self, game_state: dict) -> dict:
        game_state.update(super().play(game_state))
        game_state.update({
            'effect': 'Elite Warrior summoned to battlefield'
        })
        return game_state

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
            self.attack_power if incoming_damage > self.attack_power else 0)
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

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        spell_cost = 4
        self.mana -= spell_cost
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': spell_cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana + amount
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana': self.mana
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            'type': self.type,
            'attack': self.attack_power,
            'health': self.health,
            'mana': self.mana
        })
        return info

from .Card import Card


class CreatureCard (Card):
    """Card type - Creature,
    has attack and health attributes"""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError(f"Error creating a CreatureCard '{name}': "
                             f"Attack ({attack}) and health({health}) "
                             "attributes must be positive integers")
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        game_state.update(super().play(game_state))
        game_state.update({
            'effect': 'Creature summoned to battlefield'
        })
        return game_state

    def attack_target(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            'type': self.type,
            'attack': self.attack,
            'health': self.health
        })
        return info

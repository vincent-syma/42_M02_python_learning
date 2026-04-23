from ex0.Card import Card


class SpellCard (Card):
    """Card type - Spell,
    Processes instant magical effects,
    Has effect_type attribute (damage, heal, buff, debuff),
    Implements resolve_effect for spell mechanics,
    Spells are consumed when played (one-time use)"""

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "Spell"

    def play(self, game_state: dict) -> dict:
        game_state.update(super().play(game_state))

        effects = {
            'damage': f'Deal {self.cost} damage to target',
            'heal': f'Heal target by {self.cost} points',
            'buff': f'Buffs target with {self.cost} points',
            'debuff': f'Debuffs target of {self.cost} points'
        }

        game_state.update({
            'effect': effects[self.effect_type]
        })

        return game_state

    def resolve_effect(self, targets: list) -> dict:
        effects = {
            'damage': 'Deal {} damage to {}',
            'heal': 'Heal {} by {} points',
            'buff': 'Buff {} with {} points',
            'debuff': 'Debuff {} of {} points'
        }

        result = []

        for target in targets:
            if self.effect_type == "damage":
                description = (effects[self.effect_type].format
                               (self.cost, target))
                result.append(description)

            else:
                description = (effects[self.effect_type].format
                               (target, self.cost))
                result.append(description)

        return {'effects': result}

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            'type': self.type,
            'effect_type': self.effect_type,
        })
        return info

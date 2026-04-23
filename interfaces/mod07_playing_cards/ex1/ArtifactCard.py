from ex0.Card import Card

# Artifacts remain in play until destroyed # ???


class ArtifactCard (Card):
    """
    Card type - Artifact,
    • Represents permanent game modifiers
    • Has durability attribute (how long it lasts)
    • Has effect attribute describing the artifact’s permanent ability
    • Implements activate_ability for ongoing effects
    • Artifacts remain in play until destroyed
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "Artifact"

    def play(self, game_state: dict) -> dict:
        game_state.update(super().play(game_state))
        game_state.update({
            'effect': self.effect
        })
        return game_state

    def activate_ability(self) -> dict:
        return {
            'ability': 'activated',
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            'type': self.type,
            'durability': self.durability,
            'effect_type': self.effect,
        })
        return info

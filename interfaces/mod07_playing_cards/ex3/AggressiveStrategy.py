from .GameStrategy import GameStrategy


class AggressiveStrategy (GameStrategy):
    """
    Aggressive strategy:
    • Prioritizes attacking and dealing damage
    • Plays low-cost creatures first for board presence
    • Targets enemy creatures and player directly
    • Returns comprehensive turn execution results
    """

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Chooses cards from hand to be played.
        1 creature and 1 spell card can be played in 1 turn.
        Prioritizes low cost creatures and damage-type spells.
        """

        cards_played = []

        creatures = [card for card in hand if card.type == "Creature"]
        cheapest_creature = None

        if creatures:
            cheapest_creature = min(creatures, key=lambda c: c.cost)
            cards_played.append(cheapest_creature)

        damage = 0
        if cheapest_creature:
            damage += cheapest_creature.attack

        spells = [card for card in hand if card.type == "Spell"]

        damage_spell = None
        for spell in spells:
            if spell.effect_type == "damage":
                damage_spell = spell
                break

        if damage_spell:
            cards_played.append(damage_spell)
            damage += 1

        elif spells:
            cards_played.append(spells[0])  # fallback spell

        damage_cards = [
            card for card in cards_played
            if card.type == "Creature"
            or (card.type == "Spell" and card.effect_type == "damage")
        ]

        mana_used = sum(card.cost for card in cards_played)

        targets_to_attack = self.prioritize_targets(battlefield)

        targets_attacked = targets_to_attack[:len(damage_cards)]

        return {
            'cards_played': [card.name for card in cards_played],
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage
        }

    def get_strategy_name(self) -> str:
        return "Aggressive"

    def prioritize_targets(self, available_targets: list) -> list:
        """Chooses available targets according to their enemy status"""

        targets_to_attack = []

        for target in available_targets:
            if "Enemy" in target:
                targets_to_attack.append(target)

        return targets_to_attack

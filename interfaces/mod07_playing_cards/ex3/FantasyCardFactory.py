from ex0.Card import Card
from .CardFactory import CardFactory


class FantasyCardFactory (CardFactory):
    """
    Fantasy factory:
    • Creates fantasy-themed creatures (Dragons, Goblins, etc.)
    • Creates elemental spells (Fire, Ice, Lightning)
    • Creates magical artifacts (Rings, Staffs, Crystals)
    • Supports extensible card type registration
    """

    def __init__(self, generator=None) -> None:

        from ex1.Deck import Deck
        # from tools.card_generator import CardGenerator

        self.generator = generator()  # CardGenerator()
        self.cards_created = 0

        self.deck = Deck()

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Creates CreatureCard"""

        from ex0.CreatureCard import CreatureCard

        stats = self.generator.get_creature(name_or_power)

        if stats is None:
            if name_or_power is not None:
                raise ValueError(f"Not able to create the card "
                                 f"'{name_or_power}' with provided generator")
            stats = self.generator.get_random_creature()

        self.cards_created += 1

        return CreatureCard(**stats)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Creates SpellCard"""

        from ex1.SpellCard import SpellCard

        stats = self.generator.get_spell(name_or_power)

        if stats is None:
            if name_or_power is not None:
                raise ValueError(f"Not able to create the card "
                                 f"'{name_or_power}'")
            stats = self.generator.get_random_spell()

        self.cards_created += 1

        return SpellCard(**stats)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Creates ArtifactCard"""

        from ex1.ArtifactCard import ArtifactCard

        stats = self.generator.get_artifact(name_or_power)

        if stats is None:
            if name_or_power is not None:
                raise ValueError(f"Not able to create the card "
                                 f"'{name_or_power}'")
            stats = self.generator.get_random_artifact()

        self.cards_created += 1

        return ArtifactCard(**stats)

    def create_themed_deck(self, size: int) -> dict:
        """Creates fantasy themed deck of cards"""

        import random

        creation = {
            'creatures': self.create_creature,
            'spells': self.create_spell,
            'artifacts': self.create_artifact
        }

        while len(self.deck.cards) < size:
            card_type = random.choice(list(creation.keys()))
            card = creation[card_type]()
            self.deck.add_card(card)

        return self._deck_to_dict()

    def get_supported_types(self) -> dict:
        """Return available card types according to their classification"""

        return self._deck_to_dict()

    def _deck_to_dict(self) -> dict:
        """
        Convert self.deck (Deck instance) to dict.
        """

        type_map = {
            "Creature": "creatures",
            "Spell": "spells",
            "Artifact": "artifacts"
        }

        deck_dict = {
            'creatures': [],
            'spells': [],
            'artifacts': []
        }

        for card in self.deck.cards:
            key = type_map[card.type]
            deck_dict[key].append(card.name)

        return deck_dict

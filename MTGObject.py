from typing import List, Optional
from CardType import CardType

class MTGObject:
    def __init__(self, name: str, mana_cost: Optional[str], colors: List[str], card_types: List[CardType], subtypes: List[str], supertypes: List[str], abilities: List[str]):
        self.name = name
        self.mana_cost = mana_cost
        self.colors = colors
        self.card_types = card_types
        self.subtypes = subtypes
        self.supertypes = supertypes
        self.abilities = abilities
        self.owner = None
        self.controller = None

    def set_owner(self, player):
        self.owner = player

    def set_controller(self, player):
        self.controller = player

    def __repr__(self):
        card_types_str = ' '.join(str(card_type) for card_type in self.card_types)
        return f"{self.name} ({self.mana_cost}) - {' '.join([card_types_str] + self.subtypes + self.supertypes)}"

class Card(MTGObject):
    def __init__(self, name: str, mana_cost: Optional[str], colors: List[str], card_types: List[CardType], subtypes: List[str] = [], supertypes: List[str] = [], abilities: List[str] = []):
        super().__init__(name, mana_cost, colors, card_types, subtypes, supertypes, abilities)

class Token(MTGObject):
    def __init__(self, name: str, colors: List[str], card_types: List[CardType], subtypes: List[str] = [], supertypes: List[str] = [], abilities: List[str] = []):
        super().__init__(name, None, colors, card_types, subtypes, supertypes, abilities)

class Creature(MTGObject):
    def __init__(self, name: str, mana_cost: Optional[str], colors: List[str], card_types: List[CardType], subtypes: List[str], supertypes: List[str], power: int, toughness: int, abilities: List[str] = []):
        super().__init__(name, mana_cost, colors, [CardType.CREATURE] + supertypes, subtypes, supertypes, abilities)
        self.power = power
        self.toughness = toughness
        self.damage = 0
        self.counters = []

class Spell(MTGObject):
    def __init__(self, base_card: Card):
        super().__init__(base_card.name, base_card.mana_cost, base_card.colors, base_card.card_types, base_card.subtypes, base_card.supertypes, base_card.abilities)
        self.set_owner(base_card.owner)
        self.set_controller(base_card.controller)

    def resolve(self, game):
        # Implement resolution logic specific to this spell
        print(f"Resolving spell: {self.name}")
        if "Deal 3 damage" in self.abilities:
            target = game.choose_target(self.controller)
            game.deal_damage(target, 3)

class Ability(MTGObject):
    def __init__(self, name, controller, effects):
        super().__init__(name, None, [], [], [], [], effects)
        self.controller = controller

    def resolve(self, game):
        # Implement resolution logic specific to this ability
        print(f"Resolving ability: {self.name}")
        for effect in self.abilities:
            effect.execute(game)

class Effect:
    def __init__(self, description):
        self.description = description

    def execute(self, game):
        # Implement the effect's logic
        print(f"Executing effect: {self.description}")
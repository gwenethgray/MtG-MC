from enum import Enum, auto

class CardType(Enum):
    CREATURE = auto()
    INSTANT = auto()
    SORCERY = auto()
    LAND = auto()
    ENCHANTMENT = auto()
    ARTIFACT = auto()
    PLANESWALKER = auto()
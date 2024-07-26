class Phase(Enum):
    UNTAP = auto()
    UPKEEP = auto()
    DRAW = auto()
    PRECOMBAT_MAIN = auto()
    COMBAT = auto()
    POSTCOMBAT_MAIN = auto()
    END = auto()
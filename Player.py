from Zone import *
from ManaPool import ManaPool
from MTGObject import *

class Player:
    def __init__(self, name: str):
        self.name = name
        self.zones = {
            'library': Library(),
            'hand': Hand(),
            'battlefield': Battlefield(),
            'graveyard': Graveyard(),
            'exile': Exile()
        }
        self.life_total = 20
        self.mana_pool = ManaPool()

    def draw_card(self):
        card = self.zones['library'].draw()
        if card:
            self.zones['hand'].add_card(card)

    def play_card(self, card: Card, from_zone: str):
        if card in self.zones[from_zone].cards:
            self.zones[from_zone].remove_card(card)
            self.zones['battlefield'].add_card(card)

    def add_mana_to_pool(self, color: str, amount: int):
        self.mana_pool.add_mana(color, amount)

    def pay_mana(self, cost: str) -> bool:
        # Simplified: Assumes cost like "1RR" for two red and one of any type
        generic_mana = int(''.join([c for c in cost if c.isdigit()]))
        specific_mana = defaultdict(int)
        for c in cost:
            if c.isalpha():
                specific_mana[c] += 1

        for color, needed in specific_mana.items():
            if not self.mana_pool.use_mana(color, needed):
                return False

        if not self.mana_pool.use_mana('generic', generic_mana):
            return False

        return True
class ManaPool:
    def __init__(self):
        self.mana = defaultdict(int)  # Tracks each type of mana

    def add_mana(self, color: str, amount: int):
        self.mana[color] += amount

    def use_mana(self, color: str, amount: int) -> bool:
        if self.mana[color] >= amount:
            self.mana[color] -= amount
            return True
        return False

    def __repr__(self):
        return f"Mana Pool: {dict(self.mana)}"
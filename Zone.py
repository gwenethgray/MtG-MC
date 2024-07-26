from MTGObject import Card, Token
import random

class Zone:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def select_random_card(self):
        return self.cards[random.randint(0, len(self.cards))]

    def __repr__(self) -> str:
        cards_str = "Cards: " + ", ".join(str(card) for card in self.cards)
        return cards_str


class Library(Zone):
    def draw(self) -> Optional[Card]:
        return self.cards.pop(0) if self.cards else None

    def shuffle(self):
        random.shuffle(self.cards)


class Hand(Zone):
    def __init__(self):
        super().__init__(self)


class Battlefield(Zone):
    def __init__(self):
        super().__init__(self)
        self.tokens: List[Token] = []

    def add_token(self, token: Token):
        self.tokens.append(token)

    def remove_token(self, token: Token):
        self.tokens.remove(token)

    def __repr__(self) -> str:
        cards_str = "Cards: " + ", ".join(str(card) for card in self.cards)
        tokens_str = "Tokens: " + ", ".join(str(token) for token in self.tokens)
        return cards_str + "\n" + tokens_str


class Graveyard(Zone):
    def __init__(self):
        super().__init__(self)


class Exile(Zone):
    def __init__(self):
        super().__init__(self)
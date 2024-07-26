from Player import Player
from Stack import Stack
from Phase import Phase
from MTGObject import *

class Game:
    def __init__(self, players: List[Player]):
        self.players = players
        self.turn_order = players
        self.stack = Stack()
        self.turn_player = None
        self.active_player = None
        self.phase = None
        self.effects = None

    def start_game(self):
        self.turn_player = self.players[0]  # Assuming a two-player game for simplicity
        self.active_player = self.players[0]
        self.phase = Phase.UNTAP
        # Additional setup

    def next_phase(self, phase: Phase=None):
        self.phase = phase if phase else next(self.phases)

    def pass_priority(self, player: Player=None):
        self.active_player = None

    def next_turn(self, player: Player=None):
        self.turn_player = player if player else next(self.turn_order)
        self.turn_order.remove(self.turn_player)
        self.turn_order.append(self.turn_player)
        self.active_player = self.turn_player
        self.phase = Phase.UNTAP

    def cast_spell(self, card: Card):
        if card.mana_cost and self.check_mana(card.controller, card.mana_cost):
            spell = Spell(card)
            self.stack.push(spell)
            print(f"Spell cast and pushed to stack: {spell.name}")

    def check_mana(self, player, mana_cost):
        # Placeholder for mana checking logic
        return True

    def resolve_stack(self):
        while not self.stack.is_empty():
            item = self.stack.pop()
            item.resolve(self)
            self.check_state_based_actions()

    def check_state_based_actions(self):
        for player in self.players:
            if player.life_total <= 0:
                print(f"{player.name} has died.")
            for card in player.zones['battlefield'].cards:
                if isinstance(card, Creature) and card.damage >= card.toughness:
                    player.zones['battlefield'].remove_card(card)
                    player.zones['graveyard'].add_card(card)
                    print(f"{card.name} is destroyed.")
                if isinstance(card, Creature) and card.toughness <= 0:
                    player.zones['battlefield'].remove_card(card)
                    player.zones['graveyard'].add_card(card)
                    print(f"{card.name} is destroyed.")

    def choose_target(self, controller):
        # Placeholder for target selection, could be player or creature
        return controller #.opponent  # Simplified target selection

    def deal_damage(self, target, amount):
        if isinstance(target, Player):
            target.life_total -= amount
        elif isinstance(target, Card):  # Assuming Card can represent creatures
            target.damage += amount
            if target.damage >= target.toughness:
                print(f"{target.name} is destroyed.")
        print(f"{amount} damage dealt to {target.name}.")
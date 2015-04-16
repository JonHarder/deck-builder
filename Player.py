from random import shuffle
from Kingdom import Kingdom
from Cards import *

class Player(object):
    # __init__ : Int -> Player
    def __init__(self, player_num):
        self.discard = []
        self.hand = []
        self.draw = []
        self.player_num = player_num
        self.actions = 0
        self.buys = 0
        self.coins = 0
        for _ in range(7):
            self.draw.append(Copper())
        for _ in range(3):
            self.draw.append(Estate())
        shuffle(self.draw)

    def trash_card_id(self, card_id):
        if card_id >= 0 and card_id < len(self.hand):
            self.hand.pop(card_id)
            # self.discard.append(card)

    def discard_card_id(self, card_id):
        if card_id >= 0 and card_id < len(self.hand):
            card = self.hand.pop(card_id)
            self.discard.append(card)

    # move card from hand to discard pile
    def discard_cards(self, num_cards):
        for _ in range(num_cards):
            card = self.hand.pop()
            if card:
                self.discard.append(card)

    def draw_cards(self, num_cards):
        # need to handle empty draw deck with discard
        for _ in range(num_cards):
            if not self.draw:
                # no cards in draw pile
                self.draw = self.discard[:]
                shuffle(self.draw)
                self.discard = []
            card = self.draw.pop()
            self.hand.append(card)

    def show_hand(self):
        hand_str = ""
        for idx, card in enumerate(self.hand):
            hand_str += str(idx) + ":"+str(card)
            if idx != len(self.hand)-1:
                hand_str += ", "
        return hand_str

    def start_turn(self):
        self.actions = 1
        self.buys = 1
        self.coins = 0
        self.draw_cards(5)

    def end_turn(self, table):
        """takes the table : [Card], discards cards on
        table as well as any remaining cards in hand into
        player's discard pile"""
        self.discard += table
        self.discard += self.hand
        self.hand = []

    def action_cards_left(self):
        num_cards = 0
        for card in self.hand:
            if card.name in Kingdom.actionList:
                num_cards += 1
        return num_cards

    def __repr__(self):
        return "Player: " + str(self.player_num) + "\n" +\
               "Actions: {0}\nBuys: {1}\nCoins: {2}\n".format(self.actions,\
                                                               self.buys, self.coins)\
               + "Hand: " + self.show_hand()


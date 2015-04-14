from random import shuffle
from Cards import *

class Player(object):
    def __init__(self):
        self.discard = []
        self.hand = []
        self.draw = []
        self.actions = 0
        self.buys = 0
        self.coins = 0
        for _ in range(7):
            self.draw.append(Copper())
        for _ in range(3):
            self.draw.append(Estate())
        shuffle(self.draw)

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


    def __repr__(self):
        return "Actions: {0}\nBuys: {1}\nCoins: {2}\n".format(self.actions,
                                                              self.buys,
                                                              self.coins) \
                + "Hand: " + self.show_hand()


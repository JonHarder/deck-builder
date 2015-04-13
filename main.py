from random import shuffle

class Card(object):
    """The (base?) class for all cards."""
    def __init__(self):
        self.name = "Default Card"
        self.coins = 0
        self.actions = 0
        self.buys = 0
        self.cost = 0
        self.victory_points = 0
        self.flavor = "This is the default"

    def description(self):
        return self.name + ": Cost " + str(self.cost) + \
                           "\n" + self.flavor

    def effect(self):
        pass

    def __repr__(self):
        return self.name

class Copper(Card):
    def __init__(self):
        super(Copper, self).__init__()
        self.name = "Copper"
        self.flavor = "worth 1 coin"
        self.coins = 1

class Silver(Card):
    def __init__(self):
        super(Silver, self).__init__()
        self.name = "Silver"
        self.cost = 3
        self.coins = 2
        self.flavor = "Worth 2 coins"

class Gold(Card):
    def __init__(self):
        super(Gold, self).__init__()
        self.name = "Gold"
        self.cost = 6
        self.coins = 3
        self.flavor = "Worth 3 coins"

class Estate(Card):
    def __init__(self):
        super(Estate, self).__init__()
        self.name = "Estate"
        self.cost = 2
        self.victory_points = 1
        self.flavor = "Worth 1 victory point"

class Dutchy(Card):
    def __init__(self):
        super(Dutchy, self).__init__()
        self.name = "Dutchy"
        self.cost = 5
        self.victory_points = 3
        self.flavor = "Worth 3 victory points"

class Province(Card):
    def __init__(self):
        super(Province, self).__init__()
        self.name = "Province"
        self.cost = 8
        self.victory_points = 6
        self.flavor = "Worth 6 victory points"

class Curse(Card):
    def __init__(self):
        super(Curse, self).__init__()
        self.name = "Curse"
        self.victory_points = -1
        self.flavor = "Worth -1 victory points"

class Cellar(Card):
    def __init__(self):
        super(Cellar, self).__init__()
        self.name = "Cellar"
        self.cost = 2
        self.actions = 1
        self.flavor = "Discard any number of cards.\n+1 Card per card discarded"

class Chapel(Card):
    def __init__(self):
        super(Chapel, self).__init__()
        self.cost = 2
        self.name = "Chapel"
        self.flavor = "Trash up to 4 cards from your hand."


class Player(object):
    def __init__(self):
        self.discard = []
        self.hand = []
        self.draw = []
        for _ in range(7):
            self.draw.append(Copper())
        for _ in range(3):
            self.draw.append(Estate())
        shuffle(self.draw)

    def draw_cards(self, num_cards):
        # need to handle empty draw deck with discard
        for _ in range(num_cards):
            card = self.draw.pop()
            self.hand.append(card)

    def __repr__(self):
        return str(self.hand)

if __name__ == "__main__":
    me = Player()
    print me
    me.draw_cards(5)
    print me

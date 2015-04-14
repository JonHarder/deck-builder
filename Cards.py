class Card(object):
    """The base class for all cards."""
    def __init__(self):
        self.name = "Default Card"
        self.cost = 0
        self.victory_points = 0
        self.flavor = "This is the default"

    def description(self):
        return self.name + ": Cost " + str(self.cost) + \
                           "\n" + self.flavor

    # what happens when this card is actually played from
    # your hand onto the table
    # effect : Kingdom -> [Players] -> void?
    def effect(self, kingdom, players):
        pass

    def __repr__(self):
        return self.name

class Copper(Card):
    def __init__(self):
        super(Copper, self).__init__()
        self.name = "Copper"
        self.flavor = "worth 1 coin"

    def effect(self, kingdom, players):
        players[0].coins += 1

class Silver(Card):
    def __init__(self):
        super(Silver, self).__init__()
        self.name = "Silver"
        self.cost = 3
        self.flavor = "Worth 2 coins"

    def effect(self, kingdom, players):
        players[0].coins += 2

class Gold(Card):
    def __init__(self):
        super(Gold, self).__init__()
        self.name = "Gold"
        self.cost = 6
        self.flavor = "Worth 3 coins"

    def effect(self, kingdom, players):
        players[0].coins += 3

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
        self.flavor = "Discard any number of cards.\n+1 Card per card discarded"

    def effect(self, kingdom, players):
        players[0].actions += 1
        # discard up to x cards where x is the number of cards in players
        # hand.  Draw 1 card for each card discarded this way

class Chapel(Card):
    def __init__(self):
        super(Chapel, self).__init__()
        self.cost = 2
        self.name = "Chapel"
        self.flavor = "Trash up to 4 cards from your hand."

class Moat(Card):
    def __init(self):
        super(Moat, self).__init__()
        self.cost = 2
        self.name = "Moat"
        self.flavor = "+2 Cards\nWhen another player plays an attack\n\
card, you may reveal this from your\nhand. If you do, you are\
unaffected\nby that Attack."

class Chancellor(Card):
    def __init__(self):
        super(Chancellor, self).__init__()
        self.cost = 3
        self.name = "Chancellor"
        self.flavor = "You may immediately put your deck into your\n\
discard pile."

class Village(Card):
    def __init__(self):
        super(Village, self).__init__()
        self.cost = 3
        self.name = "Village"
        self.flavor = "+1 Card\n+2 Actions"

    def effect(self, kingdom, players):
        players[0].draw_cards(1)
        players[0].actions += 2

class Woodcutter(Card):
    def __init__(self):
        super(Woodcutter, self).__init__()
        self.cost = 3
        self.name = "Woodcutter"
        self.flavor = "+1 Buy\n+2 coins"

    def effect(self, kingdom, players):
        players[0].buys += 1
        players[0].coins += 2
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
        self.name = "copper"
        self.flavor = "worth 1 coin"

    def effect(self, kingdom, players):
        players[0].coins += 1

class Silver(Card):
    def __init__(self):
        super(Silver, self).__init__()
        self.name = "silver"
        self.cost = 3
        self.flavor = "Worth 2 coins"

    def effect(self, kingdom, players):
        players[0].coins += 2

class Gold(Card):
    def __init__(self):
        super(Gold, self).__init__()
        self.name = "gold"
        self.cost = 6
        self.flavor = "Worth 3 coins"

    def effect(self, kingdom, players):
        players[0].coins += 3

class Estate(Card):
    def __init__(self):
        super(Estate, self).__init__()
        self.name = "estate"
        self.cost = 2
        self.victory_points = 1
        self.flavor = "Worth 1 victory point"

class Dutchy(Card):
    def __init__(self):
        super(Dutchy, self).__init__()
        self.name = "dutchy"
        self.cost = 5
        self.victory_points = 3
        self.flavor = "Worth 3 victory points"

class Province(Card):
    def __init__(self):
        super(Province, self).__init__()
        self.name = "province"
        self.cost = 8
        self.victory_points = 6
        self.flavor = "Worth 6 victory points"

class Curse(Card):
    def __init__(self):
        super(Curse, self).__init__()
        self.name = "curse"
        self.victory_points = -1
        self.flavor = "Worth -1 victory points"

class Cellar(Card):
    def __init__(self):
        super(Cellar, self).__init__()
        self.name = "cellar"
        self.cost = 2
        self.flavor = "Discard any number of cards.\n+1 Card per card discarded"

    def effect(self, kingdom, players):
        print "Discard any number of cards, draw 1 card each card discarded"
        players[0].actions += 1
        num_discarded = 0
        while num_discarded < len(players[0].hand):
            print "Hand:",players[0].show_hand()
            answer = raw_input("Discarded: {0}, enter card number or end: ".format(num_discarded))
            if answer == "end":
                break
            else:
                card_id = int(answer)
                players[0].discard_card_id(card_id)
                num_discarded += 1

            players[0].draw_cards(num_discarded)


            # discard up to x cards where x is the number of cards in players
            # hand.  Draw 1 card for each card discarded this way

class Chapel(Card):
    def __init__(self):
        super(Chapel, self).__init__()
        self.cost = 2
        self.name = "chapel"
        self.flavor = "Trash up to 4 cards from your hand."

    def effect(self, kingdom, players):
        print "Trash up to 4 cards from your hand."
        num_trashed = 0
        while num_trashed < 4:
            print "Hand:",players[0].show_hand()
            answer = raw_input("Trashed: {0}, enter card number or end ".format(num_trashed))
            if answer == "end":
                return
            else:
                try:
                    card_id = int(answer)
                    players[0].trash_card_id(card_id)
                    num_trashed += 1
                except ValueError:
                    print "enter card number or end"

class Moat(Card):
    def __init__(self):
        super(Moat, self).__init__()
        self.cost = 2
        self.name = "moat"
        self.flavor = "+2 Cards\nWhen another player plays an attack\n\
card, you may reveal this from your\nhand. If you do, you are\
unaffected\nby that Attack."

    def effect(self, kingdom, players):
        players[0].draw_cards(2)

class Chancellor(Card):
    def __init__(self):
        super(Chancellor, self).__init__()
        self.cost = 3
        self.name = "chancellor"
        self.flavor = "You may immediately put your deck into your\n\
discard pile."

    def effect(self, kingdom, players):
        answer = raw_input("Put entire deck into discard pile? [y/n] ")
        if answer == "y" or "Y":
            players[0].discard += players[0].draw
            players[0].draw = []
        elif answer == "n" or "N":
            return
        else:
            print "Could not recognize answer, answer y or n"
            self.effect(kingdom, players)

class Village(Card):
    def __init__(self):
        super(Village, self).__init__()
        self.cost = 3
        self.name = "village"
        self.flavor = "+1 Card\n+2 Actions"

    def effect(self, kingdom, players):
        players[0].draw_cards(1)
        players[0].actions += 2

class Woodcutter(Card):
    def __init__(self):
        super(Woodcutter, self).__init__()
        self.cost = 3
        self.name = "woodcutter"
        self.flavor = "+1 Buy\n+2 coins"

    def effect(self, kingdom, players):
        players[0].buys += 1
        players[0].coins += 2

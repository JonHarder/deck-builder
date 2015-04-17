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
        hand_size = len(players[0].hand)
        while num_discarded < hand_size:
            print "Hand:",players[0].show_hand()
            answer = raw_input("Discarded: {0}, enter card number or end: ".format(num_discarded))
            if answer == "end":
                break
            else:
                card_id = int(answer)
                card = players[0].hand.pop(card_id)
                players[0].discard.append(card)
                # players[0].discard_card_id(card_id)
                num_discarded += 1

        players[0].draw_cards(num_discarded)

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

class Workshop(Card):
    def __init__(self):
        super(Workshop, self).__init__()
        self.cost = 3
        self.name = "workshop"
        self.flavor = "Gain a card costing up to 4"

    def effect(self, kingdom, players):
        print "Gain a card costing up to 4"
        kingdom.gain(players[0], 4)

class Bureaucrat(Card):
    def __init__(self):
        super(Bureaucrat, self).__init__()
        self.cost = 4
        self.name = "bureaucrat"
        self.flavor = "Gain a silver card;\nput it on top of your deck,\neach other player\
 reveals a victory card\nfrom his hand and puts it on his deck\n(or reveals a hand with no\
 victory cards)."

    def effect(self, kingdom, players):
        kingdom.gain_card(players[0], "silver")
        #TODO: add the other player effects


class Feast(Card):
    def __init__(self):
        super(Feast, self).__init__()
        self.cost = 4
        self.name = "feast"
        self.flavor = "Trashi this card.\nGain a card costing up to 5"

    def effect(self, kingdom, players):
        kingdom.gain(players[0], 5)

class Gardens(Card):
    def __init__(self):
        super(Gardens, self).__init__()
        self.cost = 4
        self.name = "gardens"
        self.flavor = "Worth 1 victory point\nfor every 10 cards\nin your deck (rounded down)"

class Militia(Card):
    def __init__(self):
        super(Militia, self).__init__()
        self.cost = 4
        self.name = "militia"
        self.flavor = "+2 coins\nEach other player discards\ndown to 3 cards in his hand"

    def effect(self, kingdom, players):
        players[0].coins += 2
        for player in players[1:]:
            print "Player {0}, discard down to three cards.".format(player.player_num)


class Moneylender(Card):
    def __init__(self):
        super(Moneylender, self).__init__()
        self.cost = 4
        self.name = "moneylender"
        self.flavor = "Trash a Copper card from your hand.\nIf you do, +3 coins"

    def effect(self, kingdom, players):
        for idx, card in enumerate(players[0].hand):
            if card.name == "copper":
                players[0].trash_card_id(idx)
                players[0].coins += 3
                break

class Remodel(Card):
    def __init__(self):
        super(Remodel, self).__init__()
        self.cost = 4
        self.name = "remodel"
        self.flavor = "Trash a card from your hand.\nGain a card costing up to 2 more\n\
than the trashed card."

    def effect(self, kingdom, players):
        print "Hand:", players[0].show_hand()
        card_id = int(raw_input("Enter a card number to trash: "))
        card = players[0].hand.pop(card_id)
        print "Trashing a/n", card
        max_cost = card.cost + 2
        kingdom.gain(players[0], max_cost)

class Smithy(Card):
    def __init__(self):
        super(Smithy, self).__init__()
        self.cost = 4
        self.name = "smithy"
        self.flavor = "+3 cards."

    def effect(self, kingdom, players):
        players[0].draw_cards(3)

class Spy(Card):
    def __init__(self):
        super(Spy, self).__init__()
        self.cost = 4
        self.name = "spy"
        self.flavor = "+1 Card\n+1 Action\nEach player (including you) reveals\n\
the top card of his deck and either\ndiscards it or puts it back, your choice."

from random import shuffle

class Card(object):
    """The (base?) class for all cards."""
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

    def __repr__(self):
        return "Actions: {0}\nBuys: {1}\nCoins: {2}\n".format(self.actions,
                                                              self.buys,
                                                              self.coins) \
                + "Hand: " + str(self.hand) + "\nDiscard: " + str(self.discard)

class Kingdom():
    # cards : dict<string, Card>
    treasureDict = {"copper":Copper(), "silver":Silver(), "gold":Gold(),}
    treasureList = treasureDict.keys()
    victoryDict = {"estate":Estate(), "dutchy":Dutchy(), "province":Province(),
                   "curse":Curse(),}
    victoryList = victoryDict.keys()
    actionDict = {"chapel":Chapel(), "cellar":Cellar(),
                  "moat":Moat(), "chancellor":Chancellor(),
                  "village":Village(),
                  # "woodcutter":Woodcutter(), "workshop":Workshop(),
                  # "bereaucrat":Bereaucrat(), "feast":Feast(), "gardens":Gardens(),
                  # "militia":Militia(), "moneylender":Moneylender(),
                  # "remodel":Remodel(), "smithy":Smithy(), "spy":Spy(),
                  # "thief":Thief(), "throneroom":Throneroom(),
                  # "councilroom":Councilroom(), "festival":Festival(),
                  # "laboratory":Laboratory(), "library":Library(),
                  # "market":Market(), "mine":Mine(), "witch":Witch(),
                  # "adventurer":Adventurer(),
                  }
    actionList = actionDict.keys()
    kingdomDict = {}
    kingdomDict.update(actionDict)
    kingdomDict.update(treasureDict)
    kingdomDict.update(victoryDict)
    def __init__(self):
        new_kingdom = Kingdom.actionList[:]
        shuffle(new_kingdom)
        # kingdomList : [string]
        kingdomList = new_kingdom[:10]
        # add action cards in stacks of 10
        # self.kingdom : dict<string, [Card]>
        self.kingdom = {}
        for card in Kingdom.actionList:
            self.kingdom[card] = [Kingdom.kingdomDict[card]] * 10
        self.kingdom.update({"curse":[Curse()]*10})
        self.kingdom.update({"copper":[Copper()]*40})
        self.kingdom.update({"silver":[Silver()]*35})
        self.kingdom.update({"gold":[Gold()]*30})
        self.kingdom.update({"estate":[Estate()]*8})
        self.kingdom.update({"dutchy":[Dutchy()]*8})
        self.kingdom.update({"province":[Province()]*8})

    # buy : Card -> Player -> Bool
    def buy(self, player, card):
        """takes a player and a card that player wishes to buy,
        if the card is in stock, and the player has both the buys
        and coins to get it, the player gains that card, depleting
        the kingdom of it.

        returns True if purchase occurs, False if card isn't in stock
        or player cant buy/afford card"""
        # if theres any cards left of that type
        if not self.kingdom[card]:
            return False
        if player.buys < 1:
            return False
        card_cost = self.kingdom[card][0].cost
        if player.coins < card_cost:
            return False
        # if we get here, all the conditions are met to buy the card
        # so now we do so
        bought_card = self.kingdom[card].pop()
        player.discard.append(bought_card)
        player.buys -= 1
        player.coins -= card_cost
        return True

if __name__ == "__main__":
    me = Player()
    players = [me]
    players[0].coins = 5
    players[0].buys = 2
    print players[0]
    k = Kingdom()
    k.buy(players[0], "chapel")
    print players[0]

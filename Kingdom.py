from Cards import *

from random import shuffle

class Kingdom():
    # cards : dict<string, Card>
    treasureDict = {"copper":Copper(), "silver":Silver(), "gold":Gold(),}
    treasureList = treasureDict.keys()
    victoryDict = {"estate":Estate(), "dutchy":Dutchy(), "province":Province(),
                   "curse":Curse(),}
    victoryList = victoryDict.keys()
    actionDict = {"chapel":Chapel(), "cellar":Cellar(),
                  "moat":Moat(), "chancellor":Chancellor(),
                  "village":Village(), "woodcutter":Woodcutter(),
                  # "workshop":Workshop(),
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


    # purchase : IO Card
    def purchase(self):
        selection = raw_input("Enter card name:")
        if selection == "end":
            return selection
        return Kingdom.kingdomDict[selection]

    # buy : Player -> Card -> Bool
    def buy(self, player, card):
        """takes a player and a card that player wishes to buy,
        if the card is in stock, and the player has both the buys
        and coins to get it, the player gains that card, depleting
        the kingdom of it.

        returns True if purchase occurs, False if card isn't in stock
        or player cant buy/afford card"""
        # if theres any cards left of that type
        try:
            x = self.kingdom[card]
        except KeyError:
            print "You don't have enough coins to buy that."
            return False

        if not self.kingdom[card]:
            return False
        if player.buys < 1:
            print "You don't have a buy left."
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

    # gain : Player -> Card -> Bool
    def gain(self, player, card):
        """gives the player the specific card from the kingdom,
        this is different from buying in that the player does not need
        buys or coins to aquire this card, nor will the players buys nor
        coins be affected by this act

        if card is in stock, the card will be gained and returns True
        if not, nothing will happend and return False"""
        if not self.kingdom[card]:
            return False
        gained_card = self.kingdom[card].pop()
        player.discard.append(gained_card)
        return True

    def __repr__(self):
        names = ""
        num_printed = 0
        for (name, stack) in self.kingdom.iteritems():
            num_printed += 1
            names += name + ": " + str(len(stack)) + " left\t\t"
            if num_printed == 3:
                num_printed = 0
                names += "\n"
        return names

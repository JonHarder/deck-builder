from random import shuffle

from Cards import *
from Kingdom import Kingdom
from Player import Player

# phase = ("action"|"buy")
# something : [Player] -> Kingdom -> [Card] -> String -> Bool
def play_card(players, kingdom, table, phase):
    # determine if card is action, treasure, or otherwise
    print kingdom
    print "======================================"
    print table
    print "======================================"
    print players[0]
    selection = raw_input("Play a card or type end.")
    try:
        selection = int(selection)
        card = players[0].hand[selection]
        # check to see if its an action card
        # if so, see if they actually have enough
        # actions (>= 1) to play it
        if card.name in Kingdom.victoryList:
            print "You can't play a victory card."
            return False
        if phase == "action" and card.name in Kingdom.actionList:
            if players[0].actions < 1:
                print "You dont have enough actions to play an action card"
                return False
            else:
                players[0].actions -= 1
        if phase != "action" and card.name in Kingdom.actionList:
            print "The action phase is done, you may not play another action card."
            return False
        # remove card from players hand
        players[0].hand.pop(selection)
        # put it on the table
        table.append(card)
        # play the cards effect
        card.effect(kingdom, players)
    except ValueError:
        if selection == "end":
            return "end"
        else:
            print "Invalid response. Enter a number listed next to the desired card."
            play_card(players, kingdom, table, phase)

def turn(table, kingdom, players):
    p = players[0]
    phase = "action"
    p.start_turn()

    result = ""
    while result != "end":
        if p.actions <= 0 or p.action_cards_left() == 0:
            phase = "buy"
        if phase == "buy":
            print kingdom
            print "======================"
            print table
            print "======================"
            print p
            print "======================"
            c = kingdom.purchase()
            print "Buying {0}".format(c)
        else:
            result = play_card(players, kingdom, table, phase)

    p.end_turn(table)
    players = players[1:]+[players[0]]

if __name__ == "__main__":
    table = [] # list of cards played
    kingdom = Kingdom()
    players = [Player(), Player()]
    turn(table, kingdom, players)

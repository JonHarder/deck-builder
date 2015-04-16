from random import shuffle

from Cards import *
from Kingdom import Kingdom
from Player import Player

# phase = ("action"|"buy")
# something : Int -> [Player] -> Kingdom -> String -> Bool
def play_card(card_id, players, kingdom, phase):
    # determine if card is action, treasure, or otherwise
    p = players[0]
    card = p.hand[card_id]
    # check to see if its an action card
    # if so, see if they actually have enough
    # actions (>= 1) to play it
    if card.name in Kingdom.victoryList:
        print "You can't play a victory card."
        return False
    if phase == "action" and card.name in Kingdom.actionList:
        if p.actions == 0:
            print "You dont have enough actions to play an action card"
            return False
        else:
            p.actions -= 1
    if phase != "action" and card.name in Kingdom.actionList:
        print "The action phase is done, you may not play another action card."
        return False
    # remove card from players hand
    p.hand.pop(card_id)
    # put it on the table
    table.append(card)
    # play the cards effect
    card.effect(kingdom, players)

def print_world(table, kingdom, players):
    p = players[0]
    print kingdom
    print "======================"
    print "Table:",table
    print "======================"
    print p
    print "======================"

def turn(table, kingdom, players, phase="action"):
    p = players[0]

    print_world(table, kingdom, players)

    if p.action_cards_left() == 0 or p.actions == 0:
        phase = "buy"

    selection = raw_input("[end, inspect card, play #, buy card] ")
    selection = selection.split(' ')
    if selection[0] == "inspect":
        print "------------"
        try:
            print kingdom.kingdomDict[selection[1]].description()
        except KeyError:
            print "There is no card of name {0} in the kingdom.".format(selection[1])
        print "------------"
        raw_input("Hit enter to continue.")
    if selection[0] == "buy":
        phase = "buy"
        print "------------"
        card = kingdom.kingdomDict[selection[1]]
        print card.description()
        if y_or_n("Buy Card?"):
            result = kingdom.buy(p, selection[1])
            if not result:
                print "Could not purchase a {0}".format(selection[1])
            else:
                print "Purchased a {0}".format(selection[1])
            print "------------"
            raw_input("Hit enter to continue")
        turn(table, kingdom, players, phase)
    elif selection[0] == "play":
        try:
            card_id = int(selection[1])
            play_card(card_id, players, kingdom, phase)
        except ValueError:
            print "-------------"
            print "Could not read {0} as a number".format(selection[1])
            print "-------------"
            raw_input("Hit enter to continue.")
        except IndexError:
            print "-------------"
            print "No card number given. Enter desired card like so: 'play 4'"
            print "-------------"
            raw_input("Hit enter to continue.")
        turn(table, kingdom, players, phase)
    elif selection[0] == "end":
        return
    else:
        print "action '{0}' could not be read as a recognized keyword".format(selection[0])
        turn(table, kingdom, players, phase)

def y_or_n(prompt):
    answer = raw_input(prompt + " [y/n] ")
    if answer == "y" or answer == "Y" or answer == "yes":
        return True
    elif answer == "n" or answer == "N" or answer == "no":
        return False
    else:
        print "Could not recognize answer, enter y or n"
        y_or_n(prompt)

if __name__ == "__main__":
    table = [] # list of cards played
    kingdom = Kingdom()
    players = [Player(1), Player(2)]
    while True:
        players[0].start_turn()
        turn(table, kingdom, players)
        players[0].end_turn(table)
        table = []
        p = players.pop(0)
        players.append(p)

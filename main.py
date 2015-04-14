from random import shuffle

from Cards import *
from Kingdom import Kingdom
from Player import Player

# something : [Player] -> Kingdom -> [Card] -> Bool
def something(players, kingdom, table):
    # determine if card is action, treasure, or otherwise
    print kingdom
    print "======================================"
    print table
    print "======================================"
    print players[0]
    try:
        selection = int(raw_input("Play a card: "))
        card = players[0].hand.pop(selection)
        table.append(card)
        card.effect(kingdom, players)
    except ValueError:
        print "Invalid response. Enter a number listed next to the desired card."
        something(players, kingdom, table)

if __name__ == "__main__":
    table = [] # list of cards played
    k = Kingdom()
    me = Player()
    you = Player()
    me.draw_cards(5)
    players = [me, you]
    something(players, k, table)
    something(players, k, table)

"""test data"""

# import Card Classes
from a2 import Card,SkipCard,ReverseCard,Pickup2Card,Pickup4Card

# import Player Classes
from a2 import Player,ComputerPlayer,HumanPlayer

# import Deck
from a2 import Deck

# import UnoGame
from a2_support import UnoGame

# ------------------------------------------
# p4~7 test Card


# Card and initiallize

# init function using global variable
def init():
    anna = ComputerPlayer("Anna Truffet")

    players = [anna,HumanPlayer("Henry O'Brien"),ComputerPlayer("Josh Arnold")]

    deck = Deck([Card(1,"red"), Card(2,"blue"),Card(3,"red"), Card(4,"green")])

    game = UnoGame(deck,players)

    return anna,players,deck,game



# SkipCard

# init
anna,players,deck,game = init()

print("SkipCard",end="\n\n")
card = SkipCard(0,"blue")
print(game.current_player().get_name())
print('-'*5)
card.play(anna,game)
print(game.current_player().get_name(),end="\n\n\n")
print('-'*30)


# ReverseCard

# init
anna,players,deck,game = init()

print("ReverseCard",end="\n\n")
print(game.current_player().get_name(),end="\n\n")
print(game.next_player().get_name(),end="\n\n")
print(game.next_player().get_name(),end="\n\n")
print(game.next_player().get_name(),end="\n\n")

card = ReverseCard(0,"red")
print('-'*5)
print("'card.play()'")
card.play(anna,game)
print(game.next_player().get_name(),end="\n\n")
print(game.next_player().get_name(),end="\n\n")
print(game.next_player().get_name(),end="\n\n")
print("-"*30,end="\n\n")

# Pickup2Card
anna,players,deck,game = init()

print("Pickup2Card")
print(game.next_player().get_deck().get_cards(),end="\n\n")
card = Pickup2Card(0,"red")

print("'card.play(anna,game)'")
card.play(anna,game)
print(game.next_player().get_deck().get_cards())
print("-"*30)
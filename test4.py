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
print('*'*40)


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
print('*'*40,end="\n\n")

# Pickup2Card
# assignment 上的測資怪怪的(P6)
# 底下測資是anna為current_player
# anna 的下一位是Henry 他會pickup2Card
anna,players,deck,game = init()

print("Pickup2Card")
card = Pickup2Card(0,"red")

print("game.current_player().get_name()")
print(game.current_player().get_name())

print('-'*5)

print("'card.play(anna,game)'")
card.play(anna,game)
print("\n")

print("game.current_player().get_name()")
print(game.current_player().get_name())

print(game.next_player().get_deck().get_cards())
print('*'*40,end="\n\n")


#Pickup4Card
anna,players,deck,game = init()

print("Pickup4Card")
card = Pickup4Card(0,"red")

print("game.current_player().get_name()")
print(game.current_player().get_name())

print('-'*5)

print("'card.play(anna,game)'")
card.play(anna,game)
print("\n")

print("game.current_player().get_name()")
print(game.current_player().get_name())

print(game.next_player().get_deck().get_cards())
print('*'*40,end="\n\n")

#P7 test
print("card = Card(23,'yellow')")
card = Card(23,"yellow")

print('card.__str__()')
print(card.__str__())
print('-'*5)

print('card')
print(card)
print('-'*5)

print("card = Card(42,'red')")
card = Card(42,'red')
print('card.get_number()')
print(card.get_number())
print('-'*5)

print('card.set_number(12)')
card.set_number(12)
print('-'*5)
print('card.get_number()')
print(card.get_number())
print('-'*5)

print('card.get_pick_up_amount()')
print(card.get_pickup_amount())
print('-'*5)

special_card = Pickup2Card(0,"red")

print('special_card.get_pickup_amount()')
print(special_card.get_pickup_amount())
print('-'*5)

print('special_card.matches(card)')
print(special_card.matches(card))
print('-'*5)

print('card.matchs(spical_card)')
print(card.matches(special_card))
print('-'*5)

blue_card = ReverseCard(0,"blue")

print('special_card.matches(blue_card)')
print(special_card.matches(blue_card))
print('-'*5)
print('*'*40)


# Deck
cards = [card,special_card,blue_card]
deck = Deck(cards)

print('deck.get_cards()')
print(deck.get_cards())
print('-'*5)
print('deck.get_amount()')
print(deck.get_amount())
print('-'*5)
print('deck.top()')
print(deck.top())
print('-'*5)
new_card = SkipCard(0,"green")
deck.add_card(new_card)
from os import system
system('pause')
deck.add_cards([card,special_card,blue_card])
print(deck.get_cards())
print(deck.get_amount())
print(deck.pick())
print(deck.get_amount())
print(deck.pick(amount=2))
deck.shuffle()
print(deck.get_cards())


print("*"*40)

#Player
player = Player("Peter O'Shea")

print(player.get_name())
print(player.get_deck())
print(player.get_deck().get_cards())
# player.is_playable()
print(player.has_won())
player.get_deck().add_card(Card(32,"red"))
print(player.has_won())
print("-"*5)
human = HumanPlayer("Peter Sutton")
print(human.is_playable())
print(human.pick_card(deck))

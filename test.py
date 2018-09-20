from a2 import Pickup2Card,Card,ReverseCard,SkipCard,ComputerPlayer,HumanPlayer,Pickup4Card
from a2 import Deck
import a2_support

card = Card(42,"red")

special_card = Pickup2Card(0,"red")

blue_card = ReverseCard(0,"blue")

cards = [card,special_card,blue_card]

new_card = SkipCard(0,"green")

deck = Deck(cards)
anna = ComputerPlayer("Anna")
players = [anna,HumanPlayer("Henry"),ComputerPlayer("john")]


game = a2_support.UnoGame(deck,players)

for i in game.players:
    print(i.get_name())
    print(i.get_deck().get_cards())

special_card.play(anna,game)

for i in game.players:
    print(i)
    print(i.get_name())
    print(i.get_deck().get_cards())
    print(id(i.get_deck().get_cards()))


# print("deck.get_cards()")
# print(deck.get_cards())
# print('-'*10,end="\n\n")

# print("deck.get_amount()")
# print(deck.get_amount())
# print('-'*10,end="\n\n")

# print("deck.top()")
# print(deck.top())
# print('-'*10,end="\n\n")

# deck.add_card(new_card)
# deck.add_cards([card,special_card,blue_card])
# print("deck.get_amount()")
# print(deck.get_amount())
# print('-'*10,end="\n\n")

# print("deck.get_cards()")
# print(deck.get_cards())
# print('-'*10,end="\n\n")

# print('deck.pick()')
# print(deck.pick())
# print('-'*10,end="\n\n")

# print("deck.pick(amount=2)")
# print(deck.pick(amount=2))
# print('-'*10,end="\n\n")

# print("deck.shuffle(),deck,getCard()")
# deck.shuffle()
# print(deck.get_cards())
# print('-'*10,end="\n\n")

# class test:
#     def __init__(self):
#         self.play = False
#     def play(self):
#         if self.play == True:
#             print(True)
#         elif self.play == False:
#             print(False)
#         return 'Hello'

# t = test()

# print(t.play)

# anna = ComputerPlayer("Anna")

# players = [anna,HumanPlayer("Henry"),ComputerPlayer("john")]
# deck = Deck([Card(1,"red"),Card(2,"blue"),Card(3,"red"),Card(4,"green")])
# print("deck, ",deck.get_cards())
# game = a2_support.UnoGame(deck,players)
# print(game.pickup_pile.get_cards())
# print(game)
# print(game.current_player().get_name())
# print(game.next_player().get_name())
# print(game.next_player().get_name())
# print(game.next_player().get_name())
# card.play(anna,game)
# print('-'*10)
# print(game.next_player().get_name())
# print(game.next_player().get_name())
# print(game.next_player().get_name())


# for i in range(2):
#     print(game.next_player().get_name(),end=" ")

# print('-'*10)
# card.play(anna,game)

# print(game.players)
# print(game.current_player().get_name())

# print(game.pickup_pile.get_cards())
# print(game.next_player().get_deck().get_cards())

# card.play(anna,game)

# print(game.next_player().get_deck().get_cards())
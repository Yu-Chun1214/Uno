from card import Pickup2Card,Card,ReverseCard,SkipCard
from deck import Deck


card = Card(42,"red")

special_card = Pickup2Card(0,"red")

blue_card = ReverseCard(0,"blue")

cards = [card,special_card,blue_card]

new_card = SkipCard(0,"green")

deck = Deck(cards)


print("deck.get_cards()")
print(deck.get_cards())
print('-'*10,end="\n\n")

print("deck.get_amount()")
print(deck.get_amount())
print('-'*10,end="\n\n")

print("deck.top()")
print(deck.top())
print('-'*10,end="\n\n")

deck.add_card(new_card)
deck.add_cards([card,special_card,blue_card])
print("deck.get_amount()")
print(deck.get_amount())
print('-'*10,end="\n\n")

print("deck.get_cards()")
print(deck.get_cards())
print('-'*10,end="\n\n")

print('deck.pick()')
print(deck.pick())
print('-'*10,end="\n\n")

print("deck.pick(amount=2)")
print(deck.pick(amount=2))
print('-'*10,end="\n\n")

print("deck.shuffle(),deck,getCard()")
deck.shuffle()
print(deck.get_cards())
print('-'*10,end="\n\n")

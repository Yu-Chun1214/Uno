from card import Pickup2Card,Card,ReverseCard

card = Card(42,"red")

special_card = Pickup2Card(0,"red")

blue_card = ReverseCard(0,"blue")
print(special_card.matches(blue_card))
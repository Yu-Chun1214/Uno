from a2_support import UnoGame,TurnManager
from a2 import Card,SkipCard,ReverseCard,Pickup2Card,Pickup4Card
from a2 import Player,ComputerPlayer,HumanPlayer,Deck


anna = ComputerPlayer("Anna Truffet")

players = [anna,HumanPlayer("Henry O'Brien"),ComputerPlayer("Josh Arnold")]

deck = Deck([Card(1,"red"), Card(2,"blue"),Card(3,"red"), Card(4,"green")])

game = UnoGame(deck,players)

print(game.take_turn(anna).get_name())


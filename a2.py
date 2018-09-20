#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random
# import copy
# from os import system

__author__ = "Your name & student number here"

# Write your classes here
# import copy
# import a2_support

class Card:
    colour = {'red','blue','yellow','green','black'}
    number_ = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    #Initialises Card with number and colour
    def __init__(self,number,colour):
        self.number = number
        self.colour = colour
        self.pickup_amount = 0
        self.attr = None
        self.__play = False

    def get_number(self):
        """Returns the card number"""
        return self.number
        
    def get_colour(self):
        """Returns the card colour"""
        return self.colour 

    def set_number(self, number:int):
        """Set the number value of the card"""
        self.number = number
            
    def set_colour(self,colour):
        """Set the colour of the card"""
        self.colour = colour


    def get_pickup_amount(self):
        """Returns the amount of cards the next player should pickup"""
        # if  self.pickup_amount == False:
        return self.pickup_amount

    def matches(self, card):
        """Determines if the next card to be placed on the pile
        matches this card."""
        if self.get_colour() == card.get_colour():
            return True
        elif self.get_number() == card.get_number():
            return True
        else:
            return False

    def play(self, player, game):
        """Perform a special card action. The base Card
        class has no special action."""

        if self.attr != None:
            # self.attr == 0 means that the card is skipcard
            if self.attr == 0:
                game.skip()
            
            # self.attr == -1 means that the card is reverseCard
            elif self.attr == -1:
                game.reverse()
            
            # self.attr == 2 means that the card is Pickup2Card
            elif self.attr == 2:
                # player.get_deck().add_cards(game.pickup_pile.pick(2))
                game.next_player().get_deck().add_cards(game.pickup_pile.pick(2))
                while True:
                    name = game.current_player().get_name()
                    if name == player.get_name():
                        break
                    else:
                        game.next_player()

                
            
            # self.attr == 4 means that the card is Pickup4Card
            elif self.attr == 4:
                game.next_player().get_deck().add_cards(game.pickup_pile.pick(4))
                while True:
                    name = game.current_player().get_name()
                    if name == player.get_name():
                        break
                    else:
                        game.next_player()


        return self.play
        
    def __str__(self):
        """Returns the string representation of this card."""
        return 'Card({}, {})'.format(self.number,self.colour)

        # __repr__ = __str__

    def __repr__(self):
        return 'Card({}, {})'.format(self.number, self.colour)


class SkipCard(Card):
    """A card which skips the turn of the next player.
    Matches with cards of the same colour."""
    def __init__(self,number,colour):                        
        self.number = number
        self.colour = colour
        self.pickup_amount = 0
        self.attr = 0

    def __str__(self):
        """Returns the string representation of this card."""

        return 'SkipCard({}, {})'.format(self.number, self.colour)

        # __repr__ = __str__
    def matches(self,card):
        if self.colour  == card.colour:
            return True
        else:
            return False
    def __repr__(self):
        return 'SkipCard({}, {})'.format(self.number, self.colour)
    

class ReverseCard(Card):
    """A card which skips the turn of the next player.
    Matches with cards of the same colour."""
    def __init__(self,number,colour):                        
        self.number = number
        self.colour = colour
        self.pickup_amount = 0
        # self.play = True
        self.attr = -1

    def __str__(self):
        """Returns the string representation of this card."""


        return 'ReverseCard({}, {})'.format(self.number, self.colour)

        # __repr__ = __str__
    def matches(self,card):
        if self.colour  == card.colour:
            return True
        else:
            return False
    def __repr__(self):
        return 'ReverseCard({}, {})'.format(self.number, self.colour)

   
class Pickup2Card(Card):
    """A card which makes the next player pickup two cards.
    Matches with cards of the same colour."""
    def __init__(self,number,colour):                        
        self.number = number
        self.colour = colour
        self.pickup_amount = 2
        # self.play = True
        self.attr = 2

    # def get_pickup_amount(self):
    #     return 2

    def __str__(self):
        """Returns the string representation of this card."""


        return 'Pickup2Card({}, {})'.format(self.number, self.colour)

        # __repr__ = __str__
    def matches(self,card):
        if self.colour  == card.colour:
            return True
        else:
            return False
    def __repr__(self):
        return 'Pickup2Card({}, {})'.format(self.number, self.colour)
              

class Pickup4Card(Card):
    """A card which makes the next player pickup four cards.
    Matches with any card."""
    def __init__(self,number,colour):
        self.number = number
        self.colour = colour
        self.pickup_amount = 4
        # self.play = True
        self.attr = 4

    # def get_pickup_amount(self):
    #     return 4

    def __str__(self):
        """Returns the string representation of this card."""

        return 'Pickup4Card({}, {})'.format(self.number, self.colour)

        # __repr__ = __str__
    def matches(self,card):
        return True
    def __repr__(self):
        return 'Pickup4Card({}, {})'.format(self.number, self.colour)


class Deck:
    def __init__(self,starting_cards=None):
        # import copy
        if starting_cards is None:
            self.__deck = list()
        else:
            self.__deck = starting_cards

    def get_cards(self):
        """return cards which are in deck"""
        return  self.__deck

    def get_amount(self):
        """Return the amount of card"""
        return len( self.__deck)
    
    def shuffle(self):
        """rearrange"""
        card = self.__deck[0]
        del self.__deck[0]
        self.__deck.append(card)

    def pick(self,amount:int=1):
        """return the first amount of cards off the deck and return them"""
        cards = []
        i  = 0
        if len( self.__deck) > amount: 
            # while i < amount:
            #     # print("Hello\n\n")
            #     cards.append(self.__deck.pop())
            #     i+=1
            for i in range(self.get_amount()-1,self.get_amount()-amount-1,-1):
                cards.append(self.__deck[i])
                del self.__deck[i]
        else:
            cards = [i for i in self.__deck]
            self.__deck.clear()

        return cards

    def add_card(self,card:Card):
        """add single card"""
        # import copy
        self.__deck.append(card)


    def add_cards(self,cards:list=list):
        """add lots of cards"""
        # import copy
        for i in cards:
            self.__deck.append(i)

    def top(self):
        """return the top of the card of the deck"""
        amount = self.get_amount()
        if amount == 0:
            return None
        else:
            return self.__deck[amount - 1]

    def bottom(self):
        if self.get_amount() != 0:
            return self.__deck[0]
        else:
            return None

    # def remove(self,amount:int=1):
    #     cards = []
    #     if self.get_amount() > amount:
    #         i = 0
    #         # try:
    #         print(len(self.__deck))
    #         system("pause")
    #         while i < amount:
    #             cards.append(self.__deck.pop())
    #         # except IndexError as p:
    #         #     print(len(self.__deck))
    #     else:
    #         cards = [i for i in self.__deck]
    #         self.__deck.clear()

    #     return cards
    


class Player():
    def __init__(self,name):
        self.__deck = Deck()
        self.__name = name
        self._playable = False
        self.attr = None
        

    def get_name(self):
        """Returns the name of the player."""
        return self.__name

    def get_deck(self):
        """Returns the players deck of cards."""
        return self.__deck

    def is_playable(self):
        """Returns True if the players moves aren't automatic."""
        if self._playable == False:
            raise NotImplementedError("is_playable to be implemented by subclasses")
        return self._playable
       
    def has_won(self):
        """Returns True if the player has an
        empty deck and has therefore won.
        """
        if self.__deck.get_amount() == 0:
            return True
        else:
            return False

    def pick_card(self, putdown_pile:Deck):
        """ Selects a card to play from the players current deck."""
        if self.attr is None:
            raise NotImplementedError("pick_card to be implemented by subclass") 

    


class HumanPlayer(Player):
    def __init__(self,name):
        self.__deck = Deck()
        self._playable = True
        # self.pick_card = False
        self.__name = name
        self.attr = "HumanPlayer"
    def get_deck(self):
        return self.__deck
    def get_name(self):
        return self.__name
    def pick_card(self,putdown_pile:Deck):
        return None
    def has_won(self):
        if self.__deck.get_amount() == 0:
            return True
        else: 
            return False
    def __repr__(self):
        return "HumanPlayer({})".format(self.__name)
        

class ComputerPlayer(Player):
    def __init__(self,name):
        self.__deck = Deck()
        self._playable = False
        self.__name = name
        self.attr = "ComputerPlayer"

    def pick_card(self,putdown_pile:Deck):
        pile_card = putdown_pile.top()

        i = 0
        while i <= self.__deck.get_amount():
            card = self.__deck.top()
            match = pile_card.matches(card)
            if match:
                return self.__deck.pick()[0]
            else:
                self.__deck.shuffle()
            i+=1
        return None

    def is_playable(self):
        return False
    def get_deck(self):
        return self.__deck

    def get_name(self):
        return self.__name
    
    def __repr__(self):
        return "ComputerPlayer({})".format(self.__name)
    
    def has_won(self):
        if self.__deck.get_amount() == 0:
            return True
        else:
            return False


def main():
    print("Please run gui.py instead")
    # system("python3 gui.py")




# if __name__ == "__main__":
#     main()

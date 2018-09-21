#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random

__author__ = "Your name & student number here"

# Write your classes here
class Card:
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour
        self.pickup_amount = 0

    def get_number(self):
        """ Returns the card number"""
        return self.number

    def get_colour(self):
        """ Returns the card colour"""
        return self.colour

    def set_number(self, number:int):
        """Set the number value of the card"""
        self.number = number        #set number, let this card to be..)

    def set_colour(self, colour):
        """Set the colour of the card"""
        self.colour = colour       #set colour, let this card to be..)

    def get_pickup_amount(self):
        """returns the amount of cards the next player should pick up"""
        # not including the special card
        return self.pickup_amount
        
    def matches(self, card):
        """Determines if the next card to be placed on the pile matches this card."""
        if self.get_colour() == card.get_colour():
            return True
        elif self.get_number() == card.get_number():
            return True
        else:
            return False

    def play(self, player, game):
        """ Perform a special card action"""
        pass  #normal card dont play cause only a special card action
    
    def __str__(self):
        """Returns the amount of cards the next player should pickup"""
        return 'Card(%d, %s)' % (self.number, self.colour)
    def __repr__(self):
        """Returns the amount of cards the next player should pickup"""
        return self.__str__()  #Same as __str__(self)

class SkipCard(Card):
    """A card which skips the turn of the next player. Matches with 
    cards of the same colour."""
    def __init__(self,number,colour):                        
        self.number = number
        self.colour = colour
        self.pickup_amount = 0
    
    def play(self, player, game):
        """ Perform a special card action
        """
        game.skip() #Skips the turn of next player 

    def matches(self, card):
        if self.get_colour() == card.get_colour():
            return True
        else:
            return False

    def __str__(self):
        return 'SkipCard(%d, %s)' % (self.number, self.colour)

    def __repr__(self):
        return self.__str__()

        
class ReverseCard(Card):
    """A card which reverses the order of turns.
    Matches with cards of the same colour"""
    def __init__(self,number,colour):                        
        self.number = number
        self.colour = colour
        self.pickup_amount = 0
    
    def play(self, player, game):
        """ Perform a special card action
        """
        game.reverse() #Reverses the order of turns 

    def matches(self, card):
        if self.get_colour() == card.get_colour():
            return True
        else:
            return False

    def __str__(self):
        return 'ReverseCard(%d, %s)' % (self.number, self.colour)

    def __repr__(self):
        return self.__str__()

    
class Pickup2Card(Card):
    """A card which makes the next player pickup two cards. Matches with cards of the same colour"""
    def __init__(self,number,colour):                        
        self.number = number
        self.colour = colour
        self.pickup_amount = 2  #The next player needs to pick up 2 cards

    def matches(self, card):
        if self.get_colour() == card.get_colour():
            return True
        else:
            return False
            
    def play(self, player, game):# modified
        for i in range(2):
            next_player = game.get_turns().peak()
            next_player.get_deck().add_cards(game.pickup_pile.pick())
        # next_player = game.get_turns().peak()
        # next_player.get_deck().add_cards(game.pickup_pile.pick(self.pickup_amount))
        while True:
            name = game.current_player().get_name()
            if name == player.get_name():
                break
            else:
                game.next_player()

    def __str__(self):
        return 'Pickup2Card(%d, %s)' % (self.number, self.colour)

    def __repr__(self):
        return self.__str__()


    
class Pickup4Card(Card):
    def __init__(self,number,colour):                        
        self.number = number
        self.colour = colour
        self.pickup_amount = 4 #The next player needs to pick up 4 cards
        

    def matches(self, card):#The special card Pickup4Card matches any colour
        return True
        
    def play(self, player, game):# modified
        for i in range(4):
            next_player = game.get_turns().peak()
            next_player.get_deck().add_cards(game.pickup_pile.pick())
        # next_player = game.get_turns().peak()
        # next_player.get_deck().add_cards(game.pickup_pile.pick(self.pickup_amount))
        while True:
            name = game.current_player().get_name()
            if name == player.get_name():
                break
            else:
                game.next_player()
                
    def __str__(self):
        return 'Pickup4Card(%d, %s)' % (self.number, self.colour)

    def __repr__(self):
        return self.__str__()
    


class Deck:
    def __init__(self, starting_cards=None):
        if starting_cards is None: #Players start with no cards initially 
            self.cards = list() 
        else:
            self.cards = starting_cards

    def get_cards(self):
        """Returns a list of cards in the deck."""
        return  self.cards

    def get_amount(self):
        """Returns the amount of cards in a deck."""
        return len(self.cards)

    def shuffle(self):
        '''Shuffle the oreder of the cards in the deck'''
        random.shuffle(self.cards)

    def pick(self, amount=1):
        """ Take the first 'amount' of cards off the deck
        and return them."""
       
        cards = []
        for i in range(amount):
            cards.append(self.cards[-1])
            self.cards.pop()
        return cards
            

    def add_card(self, card):
        """Place a card on top of the deck"""
        self.cards.append(card) #Add a card to the deck 

    def add_cards(self, cards):
        """Place a list of acrds on top of the deck"""
        self.cards.extend(cards) #Add a list of cards to the deck 

    def top(self):#COMMENTS 
        """Peaks at the card on top of the deck and
        returns it or None if the deck is empty."""
        amount = self.get_amount()
        if amount == 0:# amount is amount of cards in the deck if amount == 0 means that there is no card in deck
            return None
        else:
            """return the last card in the deck. 
            For example,amount == 5 means that there are 5 cards in the deck,the first is self.cards[0],
            and the last card is self.card[amount-1].
            (amount-1) - 0 + 1 is the amount of cards.
            """
            return self.cards[amount-1] 

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self._playable = False

    def get_name(self):
        """Returns the name of the player."""
        return self.name
    
    def get_deck(self):
        """Returns the players deck of cards."""
        return self.deck

    def is_playable(self):
        """Returns True iff the players moves aren't automatic."""
        if self._playable == False:
            raise NotImplementedError
        return self._playable

    def has_won(self):
        """Returns True iff the player has an empty deck and has therefore won."""
        if self.deck.get_amount() == 0:
            return True
        else:
            return False

    def pick_card(self, puutdown_pile):
        """Selects a card to play from the players current deck."""
        if self.pick_card:
            raise NotImplementedError


class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self._playable = True
    
    def pick_card(self, putdown_pile):
        return None

    

class ComputerPlayer(Player):
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self._playable = False

    def pick_card(self, putdown_pile):#COMMENTS
        """
        pile_card is the card on the top of putdown_pile
        card is the card on the top of self.deck
        every turn in whill loop below,card will be renewed

        if pile_card.matches(card) is true
        self.deck will pick the top card (statement: retrun self.deck.pick()[0])

        if pile_card.matches(card) is false
        the deck will shuffle(statement : self.deck.shuffle() )

        all cards are checked by while loop.
        the most times of while loop turn is self.deck's cards amount
        so that all cards will be checked
        
        if all card checked and cannot find the the appropriate cards
        the program will drop out the loop and return None
        """
        pile_card = putdown_pile.top()
        i = 0
        while i<= self.deck.get_amount():
            card = self.deck.top()
            if pile_card.matches(card):
                return self.deck.pick()[0]
            else:
                self.deck.shuffle()
            i+=1
        return None
        
    def is_playable(self):
        return False

def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()

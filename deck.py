from card import Card
import random

class Deck:
    def __init__(self,starting_cards=None):
        self.__deck = starting_cards

    def get_cards(self):
        """return cards which are in deck"""
        return  self.__deck

    def get_amount(self):
        """Return the amount of card"""
        return len( self.__deck)
    
    def shuffle(self):
        """rearrange"""
        self.__deck = random.sample( self.__deck,len( self.__deck))



    def pick(self,amount:int=1):
        """return the first amount of cards off the deck and return them"""
        cards = []
        i  = 0
        if len( self.__deck) > amount: 
            while i < amount:
                cards.append(self.__deck.pop())
                i+=1
        else:
            cards = [i for i in self.__deck]
            self.__deck.clear()

        return cards

    def add_card(self,card:Card):
        """add single card"""
        self.__deck.append(card)


    def add_cards(self,cards:list):
        """add lots of cards"""
        for i in cards:
            self.__deck.append(i)

    def top(self):
        """return the top of the card of the deck"""
        amount = self.get_amount()
        if amount == 0:
            return None
        else:
            return self.__deck[amount - 1]


#Player
from deck import Deck
import random

class Player():
    def __init__(self,name):
        self.deck = Deck()
        self.__name = name
        self.__playable = False
        
        
        

    def get_name(self):
        """Returns the name of the player."""
        return self.__name

    def get_deck(self):
        """Returns the players deck of cards."""
        return self.deck.get_cards()

    def is_playable(self):
        """Returns True if the players moves aren't automatic."""
        if self.__playable == True:
            raise NotImplementedError
        return self.__playable
       
    def has_won(self):
        """Returns True if the player has an
        empty deck and has therefore won.
        """
        if self.deck.get_amount() == 0:
            return True
        else:
            return False

    def pick_card(self, putdown_pile:Deck):
        """ Selects a card to play from the players current deck."""
        
        # if self.pick_card == True:
        #     if self.matches == True:
        #         self.deck.remove(card) #revomes the card
        # elif self.pick_card == False:
        #     raise NotImplementedError
        #     return None
        # elif self.matches == False:
        #     return None
        
class HumanPlayer(Player):
    def __init__(self,name):
        self.__playable == True
        self.pick_card == False
        

class ComputerPlayer(Player):
    def __init__(self,name):
        self.__playable == False
        self.pick_card == True 
        
        
        
     
        
            
        
        

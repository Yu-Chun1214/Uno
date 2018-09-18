#Player
import random

class Player():
    def __init__(self,name):
        self.name = name
        
        
        

    def get_name(self):
        """Returns the name of the player."""
        return self.name

    def get_deck(self):
        """Returns the players deck of cards."""
        return list(deck)

    def is_playable(self):
        """Returns True if the players moves aren't automatic."""
        if self.is_playable == True:
            raise NotImplementedError
        return self.is_playable
       
    def has_won(self):
        """Returns True if the player has an
        empty deck and has therefore won.
        """
        if len(deck) == '0':
            self.has_won = True
        else:
            self.has_won = False

    def pick_card(self, putdown_pile):
        """ Selects a card to play from the players current deck."""
        if self.pick_card == True:
            if self.matches == True:
                self.deck.remove(card) #revomes the card
        elif self.pick_card == False:
            raise NotImplementedError
            return None
        elif self.matches == False:
            return None
        
class HumanPlayer(Player):
    def __init__(self,name):
        self.is_playable == True
        self.pick_card == False
        

class ComputerPlayer(Player):
    def __init__(self,name):
        self.is_playable == False
        self.pick_card == True 
        
        
        
     
        
            
        
        

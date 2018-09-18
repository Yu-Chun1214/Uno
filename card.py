# import a2_support
#Card   
class Card:
    colour = {'red','blue','yellow','green','black'}
    number_ = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    #Initialises Card with number and colour
    def __init__(self,number,colour):
        self.number = number
        self.colour = colour
        self.pickup_amount = False
        self.play = False

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
        if colour == 'blue':
            self.colour = 'blue'
        elif colour == 'red':
            self.colour == 'red'
        elif colour == 'yellow':
            self.colour == 'yellow'
        elif colour == 'green':
            self.colour == 'green'
        elif colour == 'black':
            self.colour == 'black'

    def get_pickup_amount(self):
        """Returns the amount of cards the next player should pickup"""
        if  self.pickup_amount == False:
            return 0
            

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
        game = a2_support.UnoGame(deck, players)
        self.player = player
        count = 0
        if self.play == True:
            if count == '1':
                self.play = a2_support.next_player()
            elif count == '-1':
                self.play = a2_support.reverse()
        return self.play
        
    def __str__(self):
        """Returns the string representation of this card."""


        return 'Card({},{})'.format(self.number, self.colour)

        # __repr__ = __str__

    def __repr__(self):
        return 'Card({},{})'.format(self.number, self.colour)
        

# It can be inherited by special card like SkipCard,ReverseCard,etc...
class SpecialCard(Card):
    def matches(self,card):
        if self.colour == card.colour:
            return True
        else:
            return False

class SkipCard(SpecialCard):
    """A card which skips the turn of the next player.
    Matches with cards of the same colour."""
    def __init__(self,number,colour):                        
        self.number = number
        self.colour = colour
        self.pickup_amount = False
        self.play = True
        count = 1

    def __str__(self):
        """Returns the string representation of this card."""


        return 'SkipCard({},{})'.format(self.number, self.colour)

        # __repr__ = __str__

    def __repr__(self):
        return 'SkipCard({},{})'.format(self.number, self.colour)
    
    


class ReverseCard(SpecialCard):
    """A card which skips the turn of the next player.
    Matches with cards of the same colour."""
    def __init__(self,number,colour):                        
        self.number = number
        self.colour = colour
        self.pickup_amount = False
        self.play = True
        count = -1

    def __str__(self):
        """Returns the string representation of this card."""


        return 'ReverseCard({},{})'.format(self.number, self.colour)

        # __repr__ = __str__

    def __repr__(self):
        return 'ReverseCard({},{})'.format(self.number, self.colour)

   
class Pickup2Card(SpecialCard):
    """A card which makes the next player pickup two cards.
    Matches with cards of the same colour."""
    def __init__(self,number,colour):                        
        self.number = number
        self.colour = colour
        self.pickup_amount = True
        self.play = True

    def get_pickup_amount0(self):
        return 2

    def __str__(self):
        """Returns the string representation of this card."""


        return 'Pickup2Card({},{})'.format(self.number, self.colour)

        # __repr__ = __str__

    def __repr__(self):
        return 'Pickup2Card({},{})'.format(self.number, self.colour)
              

class Pickup4Card(SpecialCard):
    """A card which makes the next player pickup four cards.
    Matches with any card."""
    def __init__(self,number,colour):
        self.number = number
        self.colour = colour
        self.pickup_amount = True
        self.play = True

    def get_pickup_amount(self):
        return 4

    def __str__(self):
        """Returns the string representation of this card."""


        return 'Pickup4Card({},{})'.format(self.number, self.colour)

        # __repr__ = __str__

    def __repr__(self):
        return 'Pickup4Card({},{})'.format(self.number, self.colour)

#from a2_support
class TurnManager:
    """
    A class to manage the order of turns amongst game players.
    """
    def __init__(self, players):
        """
        Construct a new turn manager to based on game players.

        Parameters:
             players (list<T>): An ordered list of players to store.
        """
        self._players = players
        # start in correct direction
        self._direction = True
        self._location = 0
        self._max = len(players)

    def current(self):
        """
        (T) Returns the player whose turn it is.
        """
        return self._players[self._location]

    def next(self):
        """
        (T) Moves onto the next players turn and return that player.
        """
        return self.skip(count=0)

    def peak(self, count=1):
        """
        Look forward or backwards in the current ordering of turns.

        Parameters:
            count (int): The amount of turns to look forward,
                         if negative, looks backwards.

        Returns:
            (T): The player we are peaking at.
        """
        location = self._location
        location += count if self._direction else -count
        location %= self._max
        return self._players[location]

    def reverse(self):
        """
        Reverse the order of turns.
        """
        self._direction = not self._direction

    def skip(self, count=0):
        """
        (T): Moves onto the next player, skipping 'count' amount players.
        """
        count += 1
        self._location += count if self._direction else -count
        self._location %= self._max
        return self._players[self._location]





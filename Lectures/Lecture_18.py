class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self,other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __ne__(self,other):
        result = self.__eq__(other)
        return not result

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get(self):
        return (self.x,self.y)
    def set(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'

#1. an obj of type point is created
#2. the address of that obj is stored in variable/parameter self
#3. calls__init__ method of that class

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return 'Card(' + self.rank + ',' + self.suit + ')'

    def __eq__(c1, c2):
        if isinstance(c2, Card):
            return c1.rank == c2.rank and c1.suit == c2.suit
        return False
    
    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit


        
class Deck:
    def __init__(self):
        suits = {'\u2660','\u2661','\u2662', '\u2663'}
        ranks = {'A','2','3','4','5','6','7','8','9','10','J', 'Q', 'K'}
        self.deck = []
        for i in suits:
            for j in ranks:
                self.deck.append(Card(j, i))

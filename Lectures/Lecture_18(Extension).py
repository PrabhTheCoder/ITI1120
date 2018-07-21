import random

from enum import Enum

class Card:

    def __init__(self, rank, suit):
        self._rank = rank
        if isinstance(suit, Suit):
            suit = suit.value
        self._suit = suit

    def __repr__(self):
        return 'Card(' + self.rank + ',' + self.suit + ')'
    
    def __eq__(c1, c2):
        if isinstance(c2, Card):
            return c1.rank == c2.rank and c1.suit == c2.suit
        return False

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self,value):
        self._rank = value

    @rank.deleter
    def rank(self):
        del self._rank

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        self._suit = value

    @suit.deleter
    def suit(self):
        del self._suit

        
class Deck:
    def __init__(self):
        suits = {Suit.CLOVER, Suit.HEART, Suit.DIAMOND, Suit.SPADE}
        ranks = {'A','2','3','4','5','6','7','8','9','10','J', 'Q', 'K'}
        self.deck = []
        for i in suits:
            for j in ranks:
                self.deck.append(Card(j, i))
        random.shuffle(self.deck)

class Suit(Enum):
    SPADE = "\u2660"
    HEART = "\u2661"
    DIAMOND = "\u2662"
    CLOVER = "\u2663"

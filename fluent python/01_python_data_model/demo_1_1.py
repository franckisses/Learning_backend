import collections
import numpy

Card  = collections.namedtuple('Card',['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2,11) ] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self.__card = [
            Card(rank,suit) for suit in self.suits
            for rank in self.ranks 
        ]

    def __len__(self):
        return len(self.__card)

    def __getitem__(self, position):
        return self.__card[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_link(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

"""
>>> from demo_1_1 import *
>>> beer_card = Card('7','diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')
>>> deck = FrenchDeck()
>>> len(deck)
52
>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[-1]
Card(rank='A', suit='hearts')
>>> from random import choice
>>> choice(deck)
Card(rank='5', suit='clubs')
>>> deck
<demo_1_1.FrenchDeck object at 0x7ffa8d2c7a20>
>>> deck[:3]
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
"""

"""
for card in sorted(deck, key=spades_link):
    print(card)
"""


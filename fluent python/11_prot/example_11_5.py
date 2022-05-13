# -*- coding: utf-8 -*-

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                         for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

"""
>>> from example_11_5 import *
>>> deck = FrenchDeck()
>>> deck[1]
Card(rank='3', suit='spades')
>>> deck[:5]
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades'), Card(rank='5', suit='spades'), Card(rank='6', suit='spades')]
>>> from random import shuffle
>>> def set_card(dech, position, card):
...     deck._cards[position] = card
...
>>> FrenchDeck.__setitem__ = set_card
>>> shuffle(deck)
>>> deck
<example_11_5.FrenchDeck object at 0x7fdd3f5c7cc0>
>>> deck[:5]
[Card(rank='2', suit='spades'), Card(rank='4', suit='diamonds'), Card(rank='2', suit='diamonds'), Card(rank='9', suit='diamonds'), Card(rank='6', suit='clubs')]
>>>
"""

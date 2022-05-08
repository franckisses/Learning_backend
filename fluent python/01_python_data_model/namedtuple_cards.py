import collections 

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]




commond = """
>>> from examply_1_1 import FrenchDeck,Card
>>> beer_card = Card('7','diamond')
>>> beer_card
Card(rank='7', suit='diamond')
>>> deck = FrenhDeck()
>>> len(deck)
52
>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[-1]
Card(rank='A', suit='hearts')
>>> from random import choice
>>> choice(deck)
Card(rank='K', suit='spades')
>>> choice(deck)
Card(rank='4', suit='diamonds')
>>> deck
<examply_1_1.FrenhDeck object at 0x7fac46ac7a90>
>>> deck[:3]
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
>>> deck[12::13]
[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
>>> for card in deck: # doctest: +ELLIPSIS
...     print(card)
... 
Card(rank='2', suit='spades')
Card(rank='3', suit='spades')
Card(rank='4', suit='spades')
Card(rank='5', suit='spades')


>>> for card in sorted(deck, key=spades_high): # doctest: +ELLIPSIS
     ...      print(card)
     Card(rank='2', suit='clubs')
     Card(rank='2', suit='diamonds')
     Card(rank='2', suit='hearts')
     ......
     Card(rank='A', suit='diamonds')
     Card(rank='A', suit='hearts')
     Card(rank='A', suit='spades')
     ......
"""
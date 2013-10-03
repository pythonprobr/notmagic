#!/usr/bin/env python3

"""
    >>> baralho = Baralho()
    >>> len(baralho)
    52
    >>> baralho[0]
    Carta(valor='2', naipe='paus')
    >>> baralho[-1]
    Carta(valor='A', naipe='espadas')
    >>> from random import choice
    >>> choice(baralho)                 #doctest:+SKIP
    Carta(valor='4', naipe='paus')
    >>> choice(baralho)                 #doctest:+SKIP
    Carta(valor='A', naipe='espadas')
    >>> choice(baralho)                 #doctest:+SKIP
    Carta(valor='8', naipe='espadas')
    >>> baralho[:5]                     #doctest:+NORMALIZE_WHITESPACE
    [Carta(valor='2', naipe='paus'), Carta(valor='3', naipe='paus'), 
     Carta(valor='4', naipe='paus'), Carta(valor='5', naipe='paus'), 
     Carta(valor='6', naipe='paus')]
    >>> baralho[-3:]                    #doctest:+NORMALIZE_WHITESPACE
    [Carta(valor='Q', naipe='espadas'), 
     Carta(valor='K', naipe='espadas'), 
     Carta(valor='A', naipe='espadas')]
    >>> for carta in baralho:            #doctest:+ELLIPSIS
    ...   print(carta)
    ...
    Carta(valor='2', naipe='paus')
    Carta(valor='3', naipe='paus')
    Carta(valor='4', naipe='paus')
    ...
    Carta(valor='Q', naipe='espadas')
    Carta(valor='K', naipe='espadas')
    Carta(valor='A', naipe='espadas')

To generate a reversed listing:

::

    >>> for carta in reversed(baralho):         #doctest:+ELLIPSIS
    ...   print(carta)
    ...
    Carta(valor='A', naipe='espadas')
    Carta(valor='K', naipe='espadas')
    Carta(valor='Q', naipe='espadas')
    ...
    Carta(valor='4', naipe='paus')
    Carta(valor='3', naipe='paus')
    Carta(valor='2', naipe='paus')

For a numbered listing, we use `enumerate`:

::
    >>> for n, carta in enumerate(baralho, 1):  #doctest:+ELLIPSIS
    ...     print(format(n, '2'), carta)
    ...
     1 Carta(valor='2', naipe='paus')
     2 Carta(valor='3', naipe='paus')
     3 Carta(valor='4', naipe='paus')
    ...
    50 Carta(valor='Q', naipe='espadas')
    51 Carta(valor='K', naipe='espadas')
    52 Carta(valor='A', naipe='espadas')

Get all the Jacks in a baralho.
::

    >>> [carta for carta in baralho if carta.valor=='J']
    [Carta(valor='J', naipe='paus'), Carta(valor='J', naipe='ouros'), Carta(valor='J', naipe='copas'), Carta(valor='J', naipe='espadas')]

Ranking by alternate color naipes: ouros (lowest), followed by paus, copas, and espadas (highest).

    >>> hand = [Carta(valor='2', naipe='ouros'), Carta(valor='2', naipe='paus'),
    ...         Carta(valor='3', naipe='ouros'), Carta(valor='3', naipe='paus'),
    ...         Carta(valor='A', naipe='espadas')]
    >>> [cores_alternadas(carta) for carta in hand]
    [0, 1, 4, 5, 51]

    >>> hand = [Carta(valor='A', naipe='espadas'),
    ...         Carta(valor='K', naipe='ouros'),
    ...         Carta(valor='A', naipe='ouros')]
    >>> for carta in sorted(hand,key=cores_alternadas):
    ...      print(carta)
    Carta(valor='K', naipe='ouros')
    Carta(valor='A', naipe='ouros')
    Carta(valor='A', naipe='espadas')
    >>> for carta in sorted(baralho, key=cores_alternadas):   #doctest:+ELLIPSIS
    ...      print(carta)
    Carta(valor='2', naipe='ouros')
    Carta(valor='2', naipe='paus')
    Carta(valor='2', naipe='copas')
    Carta(valor='2', naipe='espadas')
    Carta(valor='3', naipe='ouros')
    ...
    Carta(valor='A', naipe='copas')
    Carta(valor='A', naipe='espadas')
    >>> from random import shuffle
    >>> shuffle(baralho)
    

"""

import collections

Carta = collections.namedtuple('Carta', ['valor', 'naipe'])

class Baralho:
    valores = [str(n) for n in range(2,11)] + list('JQKA')
    naipes = 'paus ouros copas espadas'.split()
    def __init__(self):
        self.cartas = [Carta(v, n) for n in self.naipes for v in self.valores]
    def __len__(self):
        return len(self.cartas)
    def __getitem__(self, posicao):
        return self.cartas[posicao]
    def __setitem__(self, posicao, carta):
        self.cartas[posicao] = carta

def cores_alternadas(carta):
    valor_value = Baralho.valores.index(carta.valor)
    naipes = 'ouros paus copas espadas'.split()
    return valor_value * len(naipes) + naipes.index(carta.naipe)

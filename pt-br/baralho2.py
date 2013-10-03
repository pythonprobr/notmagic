#!/usr/bin/env python3

"""
    >>> baralho = Baralho2()
    >>> baralho[:3]                     #doctest:+NORMALIZE_WHITESPACE
    [Carta(valor='2', naipe='paus'), 
     Carta(valor='3', naipe='paus'), 
     Carta(valor='4', naipe='paus')] 
    >>> zape = Carta(valor='4', naipe='paus')
    >>> zape in baralho
    True
    >>> baralho.index(zape)
    2
    >>> baralho.count(zape)
    1

"""

import collections

Carta = collections.namedtuple('Carta', ['valor', 'naipe'])

class Baralho2(collections.abc.Sequence):
    valores = [str(n) for n in range(2,11)] + list('JQKA')
    naipes = 'paus ouros copas espadas'.split()
    def __init__(self):
        self.cartas = [Carta(v, n) for n in self.naipes for v in self.valores]
    def __len__(self):
        return len(self.cartas)
    def __getitem__(self, posicao):
        return self.cartas[posicao]

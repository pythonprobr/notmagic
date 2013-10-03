
"""
    >>> p1 = Vetor(2,1)
    >>> p2 = Vetor(3,1)
    >>> p1.distancia(p2)
    1.0
    >>> pos = Vetor(2,4)
    >>> vel = Vetor(2,1)
    >>> pos + vel
    Vetor(4, 5)
    >>> vel = Vetor(3, 4)
    >>> vel * 3
    Vetor(9, 12)
    >>> 3 * vel
    Vetor(9, 12)
    
A operação a seguir não pode ser aceita, pois estamos usando * para 
representar a multiplicação escalar e não o produto vetorial. Além disso,
o resultado não faz sentido::
    
    >>> Vetor(1, 2) * Vetor(3, 4)
    Vetor(Vetor(3, 4), Vetor(6, 8))
        
"""
from math import sqrt

class Vetor:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vetor(%s, %s)' % (self.x, self.y)

    def distancia(self, v2):
        dx = self.x - v2.x
        dy = self.y - v2.y
        return sqrt(dx*dx + dy*dy)

    def __abs__(self):
        return self.distancia(Vetor(0,0))

    def __add__(self, v2):
        x = self.x + v2.x
        y = self.y + v2.y
        return Vetor(x, y)

    def __mul__(self, n):
        return Vetor(self.x*n, self.y*n)
        
    def __rmul__(self, n):
        return self * n
        

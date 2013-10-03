
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
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'Vetor' and 'Vetor'

Aqui demonstramos que, na falta de métodos específicos, Python implementa
`x *= y` como `x = x * y`, ou seja produzindo um novo objeto::

    >>> vel = Vetor(3, 4)
    >>> id(vel)  # doctest: +SKIP
    4313270928
    >>> id_vel = id(vel)
    >>> vel *= 5
    >>> vel
    Vetor(15, 20)
    >>> id(vel) == id_vel
    False

"""
from math import sqrt
from numbers import Real

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
        if isinstance(n, Real):
            return Vetor(self.x*n, self.y*n)
        else:
            return NotImplemented
        
    def __rmul__(self, n):
        return self * n
        

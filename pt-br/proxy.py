"""
    >>> t = Treco(5, 'azul', 80)
    >>> t.cor
    'azul'
    >>> t._valor
    80.0
    >>> t.preciosidade()
    16.0
    >>> t.bla
    Traceback (most recent call last):
      ...
    AttributeError: Treco instance has no attribute 'bla'
    >>> pr = Proxy(t)
    >>> pr.cor
    'azul'
    >>> pr.preciosidade()
    16.0
    >>> pr._valor
    Traceback (most recent call last):
      ...
    AttributeError: Atributo inexistente ou protegido: '_valor'

"""


class Treco:

    def __init__(self, peso, cor, valor):
        self.peso = peso
        self.cor = cor
        self._valor = float(valor)

    def preciosidade(self):
        return self._valor / self.peso
        
class Proxy:
    
    def __init__(self, embrulhado):
        self._embrulhado = embrulhado
    
    def __getattr__(self, nome_atr):
        if nome_atr.startswith('_'):
            msg = 'Atributo inexistente ou protegido: %r'
            raise AttributeError(msg % nome_atr)
        else:
            return getattr(self._embrulhado, nome_atr)
            
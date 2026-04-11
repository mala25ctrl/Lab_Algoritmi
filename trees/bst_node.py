from __future__ import annotations

class BSTNode:
    """
    Rappresenta un nodo in un Albero Binario di Ricerca.

    Attributes:
        key: il valore memorizzato nel nodo
        p: il riferimento al nodo genitore
        left: il riferimento al figlio sinistro
        right: il riferimento al figlio destro
    """

    def __init__(self, key: int, p: BSTNode | None = None):
        self.key = key
        self.p = p
        self.left = None
        self.right = None

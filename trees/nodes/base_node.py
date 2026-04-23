class BaseNode:
    def __init__(self, key: int, p: 'BaseNode | None' = None):
        """
        Rappresenta un nodo base per una struttura ad albero.

        Attributes:
            key: il valore memorizzato nel nodo
            p: il riferimento al nodo genitore
        """
        self.key = key
        self.p = p
        self.left = None
        self.right = None

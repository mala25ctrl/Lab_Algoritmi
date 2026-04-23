from trees.nodes.base_node import BaseNode

class AVLNode(BaseNode):
    def __init__(self, key: int):
        """
        Rappresenta il nodo di una albero AVL
        Args:
            key: il valore memorizzato nel nodo
        """
        super().__init__(key)
        self.height: int = 0  # Un nodo appena creato ha altezza 0
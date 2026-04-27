from enum import Enum
from trees.nodes.base_node import BaseNode


class Color(Enum):
    RED = 0
    BLACK = 1

class RBTNode(BaseNode):
    def __init__(self, key: int = 0):
        """
        Rappresenta il nodo di una albero rosso-nero
        Args:
            key: il valore memorizzato nel nodo
        """
        super().__init__(key)
        self.color: Color = Color.RED  # Un nodo appena creato è rosso
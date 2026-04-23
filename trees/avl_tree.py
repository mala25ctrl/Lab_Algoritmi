from trees.base_tree import TreeInterface
from trees.nodes.avl_node import AVLNode
from trees.nodes.base_node import BaseNode


class AVLTree(TreeInterface):

    def insert(self, x: BaseNode | None) -> None:
        pass

    def get_height(self) -> int:
        """
        Restituisce l'altezza dell'albero AVL
        Returns: Altezza altezza dell'albero AVL
        """
        return self._h(self.root)

    def _h(self, x: AVLNode | None) -> int:
        """
        Restituisce l'altezza del nodo x, o -1 se x è None
        Args:
            x: nodo di cui si vuole conoscere l'altezza
        Returns: Altezza l'altezza del nodo x, o -1 se x è None
        """
        return x.height if x else -1
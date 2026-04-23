from __future__ import annotations

from trees.base_tree import TreeInterface
from trees.nodes.bst_node import BSTNode


class BinarySearchTree(TreeInterface):

    def get_height(self) -> int:
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, x: BSTNode | None) -> int:
        """
        Metodo ricorsivo privato per il calcolo dell'altezza dell'albero
        Args:
            x: Nodo da cui iniziare il calcolo dell'altezza
        Returns: Altezza dell'albero
        """
        if x is None:
            return -1
        return 1 + max(self._get_height_recursive(x.left), self._get_height_recursive(x.right))

    def insert(self, key: int) -> None:
        """
        Inserisce una chiave nell'albero binario di ricerca
        Args:
            key: la chiave da inserire
        Returns: None
        """
        z = BSTNode(key)
        y: BSTNode | None = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z




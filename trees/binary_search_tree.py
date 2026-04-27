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
        self._bst_insert(z)


if __name__ == '__main__':
    tree = BinarySearchTree()

    tree.insert(4)
    tree.insert(5)
    tree.insert(6)

    print("Altezza dell'albero: " + str(tree.get_height()))

    tree.inorder_walk()

    x = tree.search(4)
    if x is not None:
        print("Nodo trovato:", x.key)

    x = tree.maximum()
    if x is not None:
        print("Nodo con chiave massima:", x.key)

    x = tree.minimum()
    if x is not None:
        print("Nodo con chiave minima:", x.key)

    nodeToDelete = tree.search(5)
    if nodeToDelete is not None:
        tree.delete(nodeToDelete)
        tree.inorder_walk()




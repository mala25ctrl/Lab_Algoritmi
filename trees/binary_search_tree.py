from __future__ import annotations

from trees.base_tree import TreeInterface
from trees.nodes.bst_node import BSTNode


class BinarySearchTree(TreeInterface):

    def get_height(self) -> int:
        if self.root is None:
            return -1
        stack = [(self.root, 0)]
        max_height = 0
        while stack:
            node, depth = stack.pop()
            max_height = max(max_height, depth)
            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))
        return max_height

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




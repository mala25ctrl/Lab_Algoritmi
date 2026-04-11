from __future__ import annotations
from trees.bst_node import BSTNode


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def inorder_walk(self):
        self._inorder_tree_walk(self.root)

    def _inorder_tree_walk(self, x: BSTNode | None):
        if x is None:
            return
        self._inorder_tree_walk(x.left)
        print(x.key)
        self._inorder_tree_walk(x.right)

    def insert(self, z: BSTNode):
        if not isinstance(z, BSTNode):
            raise TypeError("Puoi inserire solo oggetti di tipo BSTNode")
        y = None
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
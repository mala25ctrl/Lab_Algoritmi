from trees.base_tree import TreeInterface
from trees.nodes.avl_node import AVLNode


class AVLTree(TreeInterface):

    def insert(self, key: int) -> None:
        z = AVLNode(key)
        self._bst_insert(z)
        self._rebalance(z)

    def _rebalance(self, z: AVLNode) -> None:
        current = z.p
        while current is not None:
            current.height = 1 + max(self._h(current.left), self._h(current.right))
            bf = self._h(current.left) - self._h(current.right)

            if bf == 2:
                if self._h(current.left.left) >= self._h(current.left.right):  # Caso LL
                    self._rotate_right(current)
                else:  # Caso LR
                    self._rotate_left(current.left)
                    self._rotate_right(current)
            elif bf == -2:
                if self._h(current.right.right) >= self._h(current.right.left):  # Caso RR
                    self._rotate_left(current)
                else:  # Caso RL
                    self._rotate_right(current.right)
                    self._rotate_left(current)

            current = current.p

    def get_height(self) -> int:
        """
        Restituisce l'altezza dell'albero AVL
        Returns: Altezza dell'albero AVL
        """
        return self._h(self.root)

    def _h(self, x: AVLNode | None) -> int:
        """
        Restituisce l'altezza del nodo x, o -1 se x è None
        Args:
            x: nodo di cui si vuole conoscere l'altezza
        Returns: L'altezza del nodo x, o -1 se x è None
        """
        return x.height if x else -1

    def _rotate_left(self, x: AVLNode) -> None:
        y = x.right  # Imposta y
        x.right = y.left  # Sposta sottoalbero sx di y in dx di x

        if y.left is not None:
            y.left.p = x
        y.p = x.p

        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.left = x
        x.p = y

        # Aggiornamento altezze (prima x, poi y)
        x.height = 1 + max(self._h(x.left), self._h(x.right))
        y.height = 1 + max(self._h(y.left), self._h(y.right))

    def _rotate_right(self, x: AVLNode) -> None:
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
        # Aggiornamento altezze (prima x, poi y)
        x.height = 1 + max(self._h(x.left), self._h(x.right))
        y.height = 1 + max(self._h(y.left), self._h(y.right))

    def is_balanced(self) -> bool:
        """Verifica che l'albero rispetti la proprietà AVL"""
        return self._check_balanced(self.root)

    def _check_balanced(self, x: AVLNode | None) -> bool:
        if x is None:
            return True
        bf = self._h(x.left) - self._h(x.right)
        if abs(bf) > 1:
            return False
        return self._check_balanced(x.left) and self._check_balanced(x.right)


if __name__ == "__main__":
    tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]
    for k in keys:
        tree.insert(k)

    print(f"Altezza: {tree.get_height()}")
    print(f"Bilanciato: {tree.is_balanced()}")
    tree.inorder_walk()

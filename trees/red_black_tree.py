from trees.base_tree import TreeInterface
from trees.nodes.rbt_node import RBTNode, Color


class RedBlackTree(TreeInterface):

    def __init__(self):
        super().__init__()
        self.NIL = RBTNode()  # Nodo sentinella
        self.NIL.color = Color.BLACK
        self.root = self.NIL

    def get_height(self) -> int:
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, x: RBTNode) -> int:
        if x == self.NIL:
            return -1
        return 1 + max(self._get_height_recursive(x.left),
                       self._get_height_recursive(x.right))

    def insert(self, key: int) -> None:
        pass



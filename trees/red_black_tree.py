from trees.base_tree import TreeInterface
from trees.nodes.rbt_node import RBTNode, Color


class RedBlackTree(TreeInterface):

    def __init__(self):
        """
        Inizializza un albero rosso-nero con un nodo sentinella NIL nero
        """
        super().__init__()
        self.NIL = RBTNode()  # Nodo sentinella
        self.NIL.color = Color.BLACK
        self.root = self.NIL

    def get_height(self) -> int:
        if self.root == self.NIL:
            return -1
        stack = [(self.root, 0)]
        max_height = 0
        while stack:
            node, depth = stack.pop()
            max_height = max(max_height, depth)
            if node.left != self.NIL:
                stack.append((node.left, depth + 1))
            if node.right != self.NIL:
                stack.append((node.right, depth + 1))
        return max_height

    def insert(self, key: int) -> None:
        """
        Inserisce una chiave nell'albero rosso-nero
        Args:
            key: la chiave da inserire
        Returns: None
        """
        z = RBTNode(key)
        z.left = self.NIL
        z.right = self.NIL
        z.p = self.NIL

        # Fase 1: inserimento BST standard
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        # Fase 2: fixup
        self._insert_fixup(z)

    def _insert_fixup(self, z: RBTNode) -> None:
        """
        Ripristina la proprietà dell'albero rosso-nero dopo un inserimento
        Args:
            z: il nodo appena inserito
        Returns: None
        """
        while z.p.color == Color.RED:
            if z.p == z.p.p.left:  # Il padre è figlio sinistro
                y = z.p.p.right  # Zio di z
                if y.color == Color.RED:  # Caso 1: zio rosso
                    z.p.color = Color.BLACK
                    y.color = Color.BLACK
                    z.p.p.color = Color.RED
                    z = z.p.p
                else:
                    if z == z.p.right:  # Caso 2: z è figlio destro
                        z = z.p
                        self._rotate_left(z)
                    z.p.color = Color.BLACK  # Caso 3: z è figlio sinistro
                    z.p.p.color = Color.RED
                    self._rotate_right(z.p.p)
            else:  # Il padre è figlio destro (simmetrico)
                y = z.p.p.left  # Zio di z
                if y.color == Color.RED:  # Caso 1: zio rosso
                    z.p.color = Color.BLACK
                    y.color = Color.BLACK
                    z.p.p.color = Color.RED
                    z = z.p.p
                else:
                    if z == z.p.left:  # Caso 2: z è figlio sinistro
                        z = z.p
                        self._rotate_right(z)
                    z.p.color = Color.BLACK  # Caso 3: z è figlio destro
                    z.p.p.color = Color.RED
                    self._rotate_left(z.p.p)
        self.root.color = Color.BLACK

    def _rotate_left(self, x: RBTNode) -> None:
        """
        Esegue una rotazione sinistra sul nodo x
        Args:
            x: il nodo su cui eseguire la rotazione
        Returns: None
        """
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def _rotate_right(self, x: RBTNode) -> None:
        """
        Esegue una rotazione destra sul nodo x
        Args:
            x: il nodo su cui eseguire la rotazione
        Returns: None
        """
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def is_valid_rbt(self) -> bool:
        """
        Verifica che l'albero rispetti le proprietà dell'albero rosso-nero
        Returns: True se l'albero è un RBT valido, False altrimenti
        """
        if self.root == self.NIL:
            return True
        if self.root.color != Color.BLACK:  # Proprietà 2: la radice è nera
            return False
        return self._check_properties(self.root) != -1

    def _check_properties(self, x: RBTNode) -> int:
        """
        Verifica ricorsivamente le proprietà RBT calcolando la black-height
        Args:
            x: nodo da cui iniziare la verifica
        Returns: black-height del sottoalbero radicato in x, o -1 se le proprietà sono violate
        """
        if x == self.NIL:
            return 0

        if x.color == Color.RED:
            if x.left.color == Color.RED or x.right.color == Color.RED:
                return -1
        left_bh = self._check_properties(x.left)
        right_bh = self._check_properties(x.right)

        if left_bh == -1 or right_bh == -1 or left_bh != right_bh:
            return -1
        return left_bh + (1 if x.color == Color.BLACK else 0)

    def inorder_walk(self) -> None:
        """
        Attraversamento inorder dell'albero rosso-nero
        Returns: None
        """
        self._inorder_tree_walk(self.root)

    def _inorder_tree_walk(self, x: RBTNode) -> None:
        """
        Attraversamento inorder dell'albero rosso-nero
        Args:
            x: nodo da cui iniziare l'attraversamento
            Returns: None
        """
        if x == self.NIL:
            return
        self._inorder_tree_walk(x.left)
        print(x.key)
        self._inorder_tree_walk(x.right)

    def maximum(self, x: RBTNode | None = None) -> RBTNode | None:
        """
        Restituisce il nodo con chiave massima nell'albero
        Args:
            x: il nodo da cui iniziare la ricerca (se None, si parte dalla radice)
        Returns: il nodo con chiave massima, o None se l'albero è vuoto
        """
        if x is None:
            x = self.root
        if x == self.NIL:
            return None
        while x.right != self.NIL:
            x = x.right
        return x

    def minimum(self, x: RBTNode | None = None) -> RBTNode | None:
        """
        Restituisce il nodo con chiave minima nell'albero
        Args:
            x: il nodo da cui iniziare la ricerca (se None, si parte dalla radice)
        Returns: il nodo con chiave minima, o None se l'albero è vuoto
        """
        if x is None:
            x = self.root
        if x == self.NIL:
            return None
        while x.left != self.NIL:
            x = x.left
        return x

    def search(self, key: int) -> RBTNode | None:
        """
        Cerca un nodo nell'albero in base alla chiave
        Args:
            key: la chiave da cercare
        Returns: il nodo con la chiave specificata, o None se non esiste
        """
        x = self.root
        while x != self.NIL and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x if x != self.NIL else None


if __name__ == '__main__':
    tree = RedBlackTree()

    tree.insert(4)
    tree.insert(5)
    tree.insert(6)

    print("Altezza dell'albero: " + str(tree.get_height()))
    print("RBT valido: " + str(tree.is_valid_rbt()))

    tree.inorder_walk()

    node = tree.search(4)
    if node is not None:
        print("Nodo trovato:", node.key)

    node = tree.maximum()
    if node is not None:
        print("Nodo con chiave massima:", node.key)

    node = tree.minimum()
    if node is not None:
        print("Nodo con chiave minima:", node.key)

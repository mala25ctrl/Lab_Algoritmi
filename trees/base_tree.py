from abc import ABC, abstractmethod
from trees.nodes.base_node import BaseNode


class TreeInterface(ABC):

    def __init__(self):
        """
        Inizializza un albero binario di ricerca vuoto
        """
        self.root = None

    def search(self, key: int) -> BaseNode | None:
        """
        Cerca un nodo nell'albero in base alla chiave
        Args:
            key: la chiave da cercare
        Returns: un nodo nell'albero con la chiave specificata, o None se non esiste
        """
        x = self.root
        while x is not None and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    @abstractmethod
    def insert(self, key: int) -> None:
        """
        Inserisce una chiave nell'albero
        Args:
            key: la chiave da inserire
        Returns: None

        """
        pass

    @abstractmethod
    def get_height(self) -> int:
        """
        Restituisce l'altezza dell'albero
        Returns: altezza dell'albero
        """
        pass

    def inorder_walk(self) -> None:
        """Attraversamento inorder dell'albero
        Returns: None
        """
        self._inorder_tree_walk(self.root)

    def _inorder_tree_walk(self, x: BaseNode | None) -> None:
        """
        Attraversamento inorder dell'albero
        Args:
            x: nodo radice per il quale si esegue l'attraversamento
        Returns: None
        """
        if x is None:
            return
        self._inorder_tree_walk(x.left)
        print(x.key)
        self._inorder_tree_walk(x.right)

    def maximum(self, x: BaseNode | None = None) -> BaseNode | None:
        """
        Restituisce il nodo con chiave massima nell'albero
        Args:
            x: il nodo da cui iniziare la ricerca (se None, si parte dalla radice)
        Returns: il nodo con chiave massima, o None se l'albero è vuoto
        """
        if x is None:
            x = self.root
        if x is None:
            return None

        current: BaseNode = x  # Cambio di variabile per type checker
        while current.right is not None:
            current = current.right
        return current

    def minimum(self, x: BaseNode | None = None) -> BaseNode | None:
        """
        Restituisce il nodo con chiave minima nell'albero
        Args:
            x: Il nodo da cui iniziare la ricerca (se None, si parte dalla radice)
        Returns: il nodo con chiave minima, o None se l'albero è vuoto
        """
        if x is None:
            x = self.root
        if x is None:
            return None

        current: BaseNode = x  # Cambio di variabile per type checker
        while current.left is not None:
            current = current.left
        return current

    def successor(self, x: BaseNode) -> BaseNode | None:
        """
        Restituisce il nodo successore di un nodo dato
        Args:
            x: il nodo di cui trovare il successore
        Returns: il nodo successore, o None se non esiste
        """
        # Caso 1: sotto albero destro esiste
        if x.right is not None:
            return self.minimum(x.right)

        # Caso 2: risali l'albero
        current = x
        y = current.p

        while y is not None and current == y.right:
            current = y
            y = y.p

        return y

    def transplant(self, x: BaseNode, y: BaseNode | None) -> None:
        """
        Sostituisce il sotto albero radicato in x con il sotto albero radicato in y
        Args:
            x: sotto albero da sostituire
            y: sotto albero con cui si sostituisce
        Returns: None

        """
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        if y is not None:
            y.p = x.p

    def delete(self, z: BaseNode) -> None:
        """
        Elimina un nodo dall'albero
        Args:
            z: il nodo da eliminare
        Returns: None
        """
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)  # successore di z

            if y is None:
                return

            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                if y.right is not None:
                    y.right.p = y

            self.transplant(z, y)
            y.left = z.left
            if y.left is not None:
                y.left.p = y

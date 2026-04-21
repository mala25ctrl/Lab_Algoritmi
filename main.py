from trees.binary_search_tree import BinarySearchTree
from trees.bst_node import BSTNode

if __name__ == '__main__':
    tree = BinarySearchTree()

    tree.insert(BSTNode(4))
    tree.insert(BSTNode(5))
    tree.insert(BSTNode(6))

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

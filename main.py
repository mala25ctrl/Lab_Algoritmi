from trees.binary_search_tree import BinarySearchTree

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


from trees.binary_search_tree import BinarySearchTree
from trees.bst_node import BSTNode

if __name__ == '__main__':
    tree = BinarySearchTree()

    tree.insert(BSTNode(4))
    tree.insert(BSTNode(5))
    tree.insert(BSTNode(6))

    tree.inorder_walk()

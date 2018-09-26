from py_data_structures_and_algorithms.data_structures.hashtable.hash_table import HashTable
from py_data_structures_and_algorithms.data_structures.binary_search_tree.bst import BinaryTree, Node


def tree_intersection(bt1, bt2):
    """ returns list of values holes same values in two given bt
    """
    ht = HashTable()
    output = []
    queue = []
    queue.append(bt1.root)

    try:
        while queue[0] is not None:
            front = queue.pop(0)
            ht.set(front.val, front.val)
            if front.left is not None:
                queue.append(front.left)
            if front.right is not None:
                queue.append(front.right)
    except IndexError:
        queue.append(bt2.root)

    try:
        while queue[0] is not None:
            front = queue.pop(0)

            if ht.get(front.val) is not None:
                output.append(front.val)

            if front.left is not None:
                queue.append(front.left)
            if front.right is not None:
                queue.append(front.right)

    except IndexError:
        return output

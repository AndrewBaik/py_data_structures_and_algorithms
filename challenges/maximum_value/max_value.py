from py_data_structures_and_algorithms.data_structures.binary_search_tree.bst import Node, BinaryTree


def max_value(root=None):
    """ function that takes a root of a bt, traversal through the bt using breadth first and returns the highest value
    """
    if root is None:
        raise ValueError

    queue = []
    queue.append(root)
    max_val = 0

    try:
        while queue[0] is not None:
            front = queue.pop(0)
            if max_val < front.val:
                max_val = front.val

            if front.left is not None:
                queue.append(front.left)
            if front.right is not None:
                queue.append(front.right)
    except IndexError:
        return max_val

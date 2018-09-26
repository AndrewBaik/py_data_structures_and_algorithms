from .node import Node


class BinaryTree(object):
    def __init__(self, iterable=None):
        """ constructor method
        """
        self.root = None

        if iterable is not None:
            for i in range(len(iterable)):
                self.insert(iterable[i])

    def __str__(self):
        """ note for users
        """
        return f'{self.root}'

    def __repr__(self):
        """ note for devs
        """
        return f'<BST | Root: {self.root}>'

    def insert(self, value):
        """ insert a value into bt after validating its value
        """
        node = Node(value)
        if self.root is None:
            self.root = node
        current = self.root

        while current is not None:
            if current.val > node.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    return
            elif current.val < node.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    return
            else:
                return

    def pre_order(self, callable=lambda node: print(node)):
        """ Go visit, then go left and go right
        """
        def _walk(node=None):
            if node is None:
                return

            # Go Visit
            callable(node)

            # Go Left
            if node.left is not None:
                _walk(node.left)

            # Go Right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def in_order(self, callable=lambda node: print(node)):
        """ Go left, visit, then go right
        """
        def _walk(node=None):
            if node is None:
                return

            # Go Left
            if node.left is not None:
                _walk(node.left)

            # Go Visit
            callable(node)

            # Go Right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
        """ Go left, go right, then visit
        """
        def _walk(node=None):
            if node is None:
                return

            # Go Left
            if node.left is not None:
                _walk(node.left)

            # Go Right
            if node.right is not None:
                _walk(node.right)

            # Go Visit
            callable(node)

        _walk(self.root)

    def breadth_first(self, callable=lambda front: print(front)):
        """ Breadth first approach traversing through a bt
        """
        if self.root is None:
            raise ValueError

        queue = []
        queue.append(self.root)

        try:
            while queue[0] is not None:
                front = queue.pop(0)
                callable(front)
                if front.left is not None:
                    queue.append(front.left)
                if front.right is not None:
                    queue.append(front.right)
        except IndexError:
            return

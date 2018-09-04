class Node(object):
    def __init__(self, val, data=None, left=None, right=None):
        self.val = val
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

    def __repr__(self):
        return f'<Node | Value: {self.val} | Data: {self.data} | Left: {self.left} | Right: {self.right} | Parent: {self.parent}>'

    def __str__(self):
        return f'{self.val}'


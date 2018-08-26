from .node import Node


class Stack:
    """ class for Stack
    """
    def __init__(self, val_list=None):
        """ Constructor method for Stack
        """
        self.top = None
        self._length = 0

        if val_list is not None:
            for value in val_list:
                self.push(value)

    def __repr__(self):
        """ Display detail info about the stack
        """
        return f'< Stack | Top {self.top} | Length: {self._length} >'

    def __str__(self):
        """ displays the simple info about the stack
        """
        return f'{self.top} | Length: {self._length} '

    def __len__(self):
        """ Display the length of the stack
        """
        return self._length

    def push(self, value):
        """ Method which accepts a value of any type and creates a new Node in the Stack instance.
            Args:
                value (object): Any
            Return:
                Node
        """
        self.top = Node(value, self.top)
        self._length += 1
        return self.top

    def pop(self):
        """ method that removes the first Node inside the stack
        """
        temp = self.top
        self.top = temp._next
        temp._next = None
        self._length -= 1
        return temp.value

    def peek(self):
        """ Method that peeks at the top node in the stack
        """
        return self.top

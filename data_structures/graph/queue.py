class Node:
    def __init__(self, val, _next=None):
        self.val = val
        self._next = _next

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'<Node | val: {self.val} | Next: {self._next}>'


class Queue:
    """ Queue class
    """
    def __init__(self, val_list=None):
        """ Constructor for Queue
        """
        self.front = None
        self.rear = None
        self._length = 0

        if val_list is not None:
            for val in val_list:
                self.enqueue(val)

    def __len__(self):
        """ returns the length of the queue
        """
        return self._length

    def __repr__(self):
        """ returns the detail information about the queue
        """
        return f'< Queue | Front {self.front} | Rear {self.rear} | Length: {self._length} >'

    def __str__(self):
        """ returns the information about the queue
        """
        return f'{self.front} | {self.rear} | Length: {self._length} '

    def enqueue(self, val):
        """ Adds a new node into the queue
        """
        if self._length == 0:
            self.rear = Node(val)
            self.front = self.rear
        else:
            self.rear._next = Node(val)
            self.rear = self.rear._next
        self._length += 1

    def dequeue(self):
        """ Removes the last node in the queue
        """
        if self._length == 0:
            raise IndexError
        if self.front._next is None:
            temp = self.front
            self.front = None
            self.rear = None
            self._length = 0
        else:
            temp = self.front
            try:
                self.front = self.front._next
            except AttributeError:
                self.front = None
            self._length -= 1
        return temp.val

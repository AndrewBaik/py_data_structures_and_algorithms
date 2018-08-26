from .node import Node


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
            for value in val_list:
                self.enqueue(value)

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

    def enqueue(self, value):
        """ Adds a new node into the queue
        """
        self.front = Node(value, self.front)
        if self.rear is None:
            self.rear = self.front
        self._length += 1

    def dequeue(self):
        """ Removes the last node in the queue
        """
        if self.front is not self.rear:
            current = self.front
            while current._next is not self.rear:
                current = current._next
            current._next = None
            self.rear = current
        else:
            self.front, self.rear = None
        self._length -= 1

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
        self.rear = Node(val, self.front)
        if self.front is None:
            self.front = self.rear
        self._length += 1

    def dequeue(self):
        """ Removes the last node in the queue
        """
        if self.front is not self.rear:
            current = self.rear
            while current._next is not self.front:
                current = current._next
            temp = current._next
            current._next = None
            self.front = current
        else:
            temp = self.front
            self.rear, self.front = None
        self._length -= 1
        return temp

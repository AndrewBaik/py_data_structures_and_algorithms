from .node import Node


class Animal_Shelter:
    """ Animal shelter with enqueue and dequeue methods
    """
    def __init__(self):
        """ constructor with attributes
        """
        self.front = None
        self.rear = None
        self._length = 0

    def enqueue(self, animal):
        """ Adds animal object (node) into the animal shelter(queue)
        """
        node = Node(animal, self.rear)
        if self.front is None:
            self.front = node
        self.rear = node
        self._length += 1
        return node

    def dequeue(self, animal=None):
        """ if animal is specified, finds the closest animal to front and returns the object with given animal
        """
        if self.front is None:
            return None

        if self.rear is self.front:
            self.rear = None
            temp = self.front
            self.front = None
            self._length -= 1
            return temp

        current = self.rear
        if animal is None:
            while current._next is not self.front:
                current = current._next
            temp = current._next
            current._next = temp._next
            self._length -= 1
            return temp
        node = None
        if current.val is animal:
            node = current
        while current._next is not None:
            if current._next.val is animal:
                before = current
                node = current._next
            current = current._next
        if node is None:
            return node
        before._next = node._next
        self._length -= 1
        return node


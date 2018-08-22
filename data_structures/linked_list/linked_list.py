from .node import Node


class LinkedList(object):
    """ Abstract clss for linked list
    """
    def __init__(self, val_list=None):
        """ Constructor for LinkedList
        """
        self.head = None
        self._length = 0

        if val_list is not None:
            for val in val_list:
                self.insert(val)

    def __str__(self):
        return f'{self.head} | Length: {self._length}'

    def __repr__(self):
        return f'< Linked List | Head {self.head} | Length: {self._length} >'

    def __len__(self):
        return self._length

    def insert(self, val):
        """ Inserting a Node created according to its value inserted to this method
        """
        self.head = Node(val, self.head)
        self._length += 1

    def includes(self, val) -> bool:
        """ Validates if inputed value is included in the linked list
        """
        current = self.head
        while current is not None:
            if current.val is val:
                return True
            current = current._next
        return False

    def append(self, value):
        """ method that adds a new node at the end of the linked list
        """
        current = self.head
        while current._next is not None:
            current = current._next
        current._next = Node(value)
        self._length += 1

    def insertBefore(self, val, newVal):
        """ method that adds a new node before a given value of a node
        """
        if self.head.val is val:
            self.head = Node(newVal, self.head)
            self._length += 1
            return
        current = self.head
        while current._next is not None:
            if current._next.val is val:
                current._next = Node(newVal, current._next)
                self._length += 1
                return
            else:
                current = current._next

    def insertAfter(self, val, newVal):
        """ method that adds a new node after a given value of a node
        """
        current = self.head
        while current._next is not None:
            if current.val is val:
                current._next = Node(newVal, current._next)
                self._length += 1
                return
            else:
                current = current._next
        if current.val is val:
            current._next = Node(newVal)
            self._length += 1

    def kth_from_the_end(self, kth):
        """ find the kth value from the end of linked list
        """
        counter = 0
        current = self.head
        while current._next is not None:
            current = current._next
            counter += 1
        front_index = counter - kth
        current = self.head
        while front_index is not 0:
            current = current._next
            front_index -= 1
        return current.val


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4])
    ll.insertAfter(13, 5)

    current = ll.head
    while current is not None:
        print(str(current.val))
        current = current._next

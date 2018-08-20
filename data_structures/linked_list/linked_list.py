from node import Node


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
        return f'< Linked List | Head {self.head} | Length: {self.length} >'

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
        current = self.head
        while current._next.val is not val:
            current = current._next
        current._next = Node(newVal, current._next)
        self._length += 1

    def insertAfter(self, val, newVal):
        """ method that adds a new node after a given value of a node
        """
        current = self.head
        while current.val is not val:
            current = current._next
        current._next = Node(newVal, current._next)
        self._length += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert(6)
    ll.insert(7)
    ll.append(1)
    ll.insertBefore(3, 4)
    ll.insertAfter(6, 5)
    ll.current = ll.head
    while ll.current is not None:
        print(str(ll.current.val))
        ll.current = ll.current._next

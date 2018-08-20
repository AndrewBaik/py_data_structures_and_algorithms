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

    def __str(self):
        return f'{self.head} | Length: {self._length}'

    def __repr__(self):
        return f'< Linked List | Head {self.head} | Length: {self.length} >'

    def __len__(self):
        return self._length

    def insert(self, val):
        """ Inserting a Node created according to its value inserted to this method
        """
        new_node = Node(val)
        new_node._next = self.head
        self.head = new_node
        self.current = self.head
        self._length += 1

    def includes(self, val) -> bool:
        """ Validates if inputed value is included in the linked list
        """
        self.current = self.head
        while self.current is not None:
            if self.current.val is val:
                return True
            self.current = self.current._next
        return False

    def append(self, value):
        """ method that adds a new node at the end of the linked list
        """
        self.current = self.head
        while self.current._next is not None:
            self.current = self.current._next
        new_node = Node(value)
        self.current._next = new_node


def run():
    ll = LinkedList([1, 2, 3])
    print(ll.includes(1))
    print(ll.includes(2))
    print(ll.includes(3))


if __name__ == '__main__':
    run()


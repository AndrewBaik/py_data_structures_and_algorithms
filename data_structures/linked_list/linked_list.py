from .node import Node


class LinkedList(object):
    def __init__(self, val_list=None):
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
        new_node = Node(val)
        new_node._next = self.head
        self.head = new_node
        self.current = self.head
        self._length += 1

    def includes(self, val) -> bool:
        self.current = self.head
        while self.current is not None:
            if self.current.val is val:
                return True
            self.current = self.current._next
        return False


def run():
    ll = LinkedList([1, 2, 3])
    print(ll.includes(1))
    print(ll.includes(2))
    print(ll.includes(3))


if __name__ == '__main__':
    run()

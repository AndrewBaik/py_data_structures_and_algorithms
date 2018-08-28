from py_data_structures_and_algorithms.data_structures.stack.stack import Stack, Node


class Queue:
    """ Implement Queue using two Stacks
    """
    def __init__(self):
        """ Constructor for queue class
        """
        self.front = None
        self.rear = None
        self.stack1 = Stack()
        self.stack2 = Stack()
        self._length = 0

    def enqueue(self, value):
        """ Method applying enqueue functionality using stacks
        """
        node = self.stack1.push(value)
        if self.front is None:
            self.front = node
        self.rear = node
        self._length += 1
        return self

    def dequeue(self):
        """ Method applying dequeue functionality using stacks
        """
        if self.stack1.top is None and self.stack2.top is None:
            return None
        if self.stack2.top is not None:
            temp = self.stack2.pop()
            self.stack2.top = self.front
            self._length -= 1
            return temp
        current = self.stack1.top
        while current is not None:
            node_val = self.stack1.pop()
            self.stack2.push(node_val)
            current = current._next
        temp = self.stack1.pop()
        self._length -= 1
        self.stack2.top = self.front
        return temp

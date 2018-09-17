class Node(object):
    """ node used
    """
    def __init__(self, value=None):
        self.value = value
        self.neighbors = []
        self.visited = False


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


class Graph(object):
    def __init__(self):
        self.graph = {}

    def __str__(self):
        return f'<Graph | {self.graph}>'

    def __repr__(self):
        return f'<Graph | {self.graph} | Length: {len(self.graph)}>'

    def __len__(self):
        return len(self.graph)

    def add_vert(self, value):
        """ adds value to the graph
        """
        # add vertice to self.graph
        if self.has_vert(value):
            raise KeyError
        else:
            self.graph[value] = {}

    def has_vert(self, value):
        """ checks for a key in the graph returns in boolean
        """
        try:
            if self.graph[value] is not None:
                return True
        except KeyError:
            return False

    def add_edge(self, value1, value2, weight):
        """ adds a new edge between two vertices
        """
        try:
            self.graph[value1]
            self.graph[value2]
        except KeyError:
            raise KeyError

        keyvalue1 = self.graph[value1]
        keyvalue1[value2] = weight
        keyvalue2 = self.graph[value2]
        keyvalue2[value1] = weight

    def get_neighbors(self, value):
        """ Finds the all connected verticies and return in a list
        """
        #  given a value(key), return all of all adjacent vert
        if self.graph[value]:
            vertices = []
            for key in self.graph[value].keys():
                vertices.append(key)
            return vertices
        else:
            raise KeyError

    def breadth_first(self, root):
        """ returns a list of all the nodes in the graph
        """
        if root is None:
            return([])
        output = []
        for key in self.graph.keys():
            output.append(key)
        return output

    # def breadth_first_traversal(self, Node):
    #    """
    #    """
    #    if Node is None:
    #        return([])
    #    queue = Queue()
    #    output = []
    #    queue.enqueue(Node)
    #    Node.visited = True
    #    while len(queue) > 0:
    #        front = queue.dequeue()
    #        output.append(queue.dequeue().value)
    #        for i in front.neighbors:
    #            if i.visited is False:
    #                queue.enqueue(i)
    #                i.visited = True
    #    return output

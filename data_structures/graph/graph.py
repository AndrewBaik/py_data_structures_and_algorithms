from .queue import Queue


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

    def breadth_first(self, root=None):
        """ returns a list of all the nodes in the graph
        """
        if root is None:
            return []
        container = Queue()
        output = []
        container.enqueue(root)
        visited = {root: True}
        while container._length is not 0:
            value = container.dequeue()
            output.append(value)
            for node in self.graph[value]:
                try:
                    visited[node]
                except KeyError:
                    container.enqueue(node)
                    visited[node] = True
        return output

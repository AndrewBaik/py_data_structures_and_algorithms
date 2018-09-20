def depth_first_adjlist(adjlist=None):
    """ function that validates the adj list in depth first approach
    """
    if adjlist is None:
        raise AttributeError

    def recursion(adjlist, key):
        """ helper function that will be recursing
        """
        output.append(key)
        for neighbor in adjlist[key]:
            try:
                visited[neighbor]
            except KeyError:
                visited[neighbor] = True
                recursion(adjlist, neighbor)

    visited = {}
    output = []
    for key in adjlist.keys():
        try:
            visited[key]
        except KeyError:
            visited[key] = True
            recursion(adjlist, key)
    return output

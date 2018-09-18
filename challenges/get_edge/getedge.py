from py_data_structures_and_algorithms.data_structures.graph.graph import Graph


def get_edge(grp, cities):
    """ validates the connection between cities that are given and return the total amount of edges added.
    """
    total_cost = 0
    for i in range(len(cities)):
        if i < len(cities) - 1:
            try:
                if grp.graph[cities[i]] is not None:
                    city = grp.graph[cities[i]]
                    try:
                        city[cities[i+1]]
                        total_cost += city[cities[i+1]]
                    except KeyError:
                        return False, 0
                else:
                    return False, 0
            except KeyError:
                return False, 0
    return True, total_cost

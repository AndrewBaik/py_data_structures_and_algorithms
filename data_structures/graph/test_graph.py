from .graph import Graph
import pytest


@pytest.fixture
def empty_graph():
    return Graph()


@pytest.fixture
def small_graph():
    graph = Graph()
    graph.graph = {
        1: {2: 5},
        2: {1: 5},
    }
    return graph


@pytest.fixture
def connected_graph():
    graph = Graph()
    graph.graph = {
        'A': {'B': 1, 'D': 5},
        'B': {'A': 1, 'C': 3},
        'C': {'B': 3, 'D': 8},
        'D': {'A': 5, 'C': 8},
    }
    return graph


@pytest.fixture()
def filled_graph():
    graph = Graph()
    graph.graph = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }
    return graph


def test_graph_instance(empty_graph):
    """ testing for the instance of graph
    """
    assert isinstance(empty_graph, Graph)


def test_graph_attribute(empty_graph):
    """ test for attribute values of empty graph
    """
    assert empty_graph.graph == {}
    assert len(empty_graph) == 0


def test_add_vertical(empty_graph):
    """ test for adding a new value to graph
    """
    empty_graph.add_vert(5)
    empty_graph.add_vert(6)
    assert empty_graph.graph[5] == {}
    assert empty_graph.graph[6] == {}


def test_add_duplicate(empty_graph):
    """ test for adding already added value
    """
    empty_graph.add_vert(5)
    with pytest.raises(KeyError):
        empty_graph.add_vert(5)


def test_has_vert(small_graph):
    """ testing if contains the vert in the graph
    """
    assert small_graph.has_vert(1) is True


def test_has_vert_false(small_graph):
    """ testing for vert dont exist
    """
    assert small_graph.has_vert(5) is False


def test_adding_edge(filled_graph):
    """ testing adding edge between two vertices
    """
    expect = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {'F': 3},
        'F': {'E': 3}
    }
    filled_graph.add_edge('E', 'F', 3)
    assert filled_graph.graph == expect


def test_adding_edge_one_nonexist(filled_graph):
    """ test adding edge between one vertice dont exist
    """
    with pytest.raises(KeyError):
        filled_graph.add_edge('A', 'Z', 6)


def test_adding_edge_both_nonexist(filled_graph):
    """ test adding edge between both vertices dont exist
    """
    with pytest.raises(KeyError):
        filled_graph.add_edge('X', 'Z', 12)


def test_all_neighbors(filled_graph):
    """ test for getting all neighbors
    """
    expect = ['A', 'D', 'C']
    assert filled_graph.get_neighbors('B') == expect


def test_all_empty_neighbors(filled_graph):
    """ test for getting all neighbors which are empty
    """
    with pytest.raises(KeyError):
        filled_graph.get_neighbors('E')


def test_breadthfirst(connected_graph):
    """
    """
    expect = ['A', 'B', 'D', 'C']
    actual = connected_graph.breadth_first('A')
    assert actual == expect


def test_empty_root_breadth_first(connected_graph):
    """ test for bradthfirst putting empty root
    """
    expect = []
    actual = connected_graph.breadth_first()
    assert actual == expect


def test_disconnected_graph_breadthfirst(filled_graph):
    """ test for breadth first of a disconnected node
    """
    expect = ['E']
    actual = filled_graph.breadth_first('E')
    assert actual == expect

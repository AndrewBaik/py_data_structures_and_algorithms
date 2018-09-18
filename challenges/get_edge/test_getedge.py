from . getedge import get_edge, Graph
import pytest


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


def test_get_edge_expect_true(connected_graph):
    """ test for input of connect cities
    """
    expect = True, 8
    actual = get_edge(connected_graph, ['C', 'D'])
    assert expect == actual


def test_get_edge_multi_cities(connected_graph):
    """ test for input of connected four cities
    """
    expect = True, 12
    actual = get_edge(connected_graph, ['A', 'B', 'C', 'D'])
    assert expect == actual


def test_get_edge_expect_false(connected_graph):
    """ test for input of disconnect cities
    """
    expect = False, 0
    actual = get_edge(connected_graph, ['A', 'C'])
    assert expect == actual


def test_get_edge_multi_cities_false(connected_graph):
    """ test for input of partially disconnected cities
    """
    expect = False, 0
    actual = get_edge(connected_graph, ['D', 'C', 'A', 'B'])
    assert expect == actual


def test_wrong_cities(connected_graph):
    """ test for inputing cities dont exist
    """
    expect = False, 0
    actual = get_edge(connected_graph, ['F', 'E'])
    assert expect == actual

from .depth_first import depth_first_adjlist
import pytest


@pytest.fixture
def adj_list():
    adjlist = {
        'A': ['B', 'D'],
        'B': ['A', 'C'],
        'C': ['B', 'D'],
        'D': ['A', 'C'],
    }
    return adjlist


@pytest.fixture
def adj_list2():
    adjlist = {
        'D': ['A', 'C'],
        'B': ['A', 'C'],
        'A': ['B', 'D'],
        'C': ['B', 'D'],
    }
    return adjlist


def test_depth_first_graph(adj_list):
    """ test for returning correct list
    """
    expect = ['A', 'B', 'C', 'D']
    actual = depth_first_adjlist(adj_list)
    assert expect == actual


def test_depth_first_graph_different_list(adj_list2):
    """ test for returning the same adj list with different order
    """
    expect = ['D', 'A', 'B', 'C']
    actual = depth_first_adjlist(adj_list2)
    assert expect == actual


def test_depth_first_empty():
    """ test for pushing in an empty dict as an arg
    """
    with pytest.raises(AttributeError):
        depth_first_adjlist()

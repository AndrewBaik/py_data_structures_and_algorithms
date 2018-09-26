from .tree_intersection import tree_intersection
from py_data_structures_and_algorithms.data_structures.binary_search_tree.bst import BinaryTree, Node
import pytest


@pytest.fixture
def bt1():
    bt = BinaryTree(['1', '2', '3', '4', '5', '6'])
    return bt


@pytest.fixture
def bt2():
    bt = BinaryTree(['3', '6', '9', '10', '2', '5'])
    return bt


@pytest.fixture
def bt3():
    bt = BinaryTree(['6', '7', '8'])
    return bt


@pytest.fixture
def bt4():
    bt = BinaryTree(['15', '255', '1207', '1'])
    return bt


def test_return_intersections_a_value(bt1, bt3):
    """ test for returning correct list of a value
    """
    expect = ['6']
    actual = tree_intersection(bt1, bt3)
    assert expect == actual


def test_return_intersections_values(bt1, bt2):
    """ test for returning correct list of values
    """
    expect = ['3', '6', '2', '5']
    actual = tree_intersection(bt1, bt2)
    assert expect == actual


def test_return_no_value(bt2, bt4):
    """ test for returning no values
    """
    expect = []
    actual = tree_intersection(bt2, bt4)
    assert expect == actual


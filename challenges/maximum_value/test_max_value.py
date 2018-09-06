from py_data_structures_and_algorithms.data_structures.binary_search_tree.bst import BinaryTree, Node
from .max_value import max_value
import pytest


@pytest.fixture
def empty_bt():
    return Node()


@pytest.fixture
def small_bt():
    return BinaryTree([5, 2, 9])


@pytest.fixture
def balanced_bt():
    return BinaryTree([5, 3, 8, 2, 7, 4, 9])


def test_pass_in_empty_argument():
    """ tests error type when no argument has passed in
    """
    with pytest.raises(ValueError):
        max_value()


def test_pass_in_small_bt(small_bt):
    """ test the return value with small binary tree
    """
    expected = 9
    assert max_value(small_bt.root) == expected


def test_pass_in_large_bt(balanced_bt):
    """ test the balanced binary tree
    """
    expected = 9
    assert max_value(balanced_bt.root) == expected

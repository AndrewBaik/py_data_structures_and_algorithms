from .bst import BinaryTree
import pytest


@pytest.fixture
def empty_bt():
    return BinaryTree()


@pytest.fixture
def small_bt():
    return BinaryTree([5, 2, 9])


@pytest.fixture
def balanced_bt():
    return BinaryTree([5, 3, 8, 2, 7, 4, 9])


def test_instance_of_bt(empty_bt):
    """ Checks for the instance of binary tree class
    """
    assert isinstance(empty_bt, BinaryTree)


def test_value_empty_root(empty_bt):
    """ Checks for the vaule of root when bt is empty
    """
    assert empty_bt.root is None


def test_single_insertion(empty_bt):
    """ tests for inserting single value
    """
    empty_bt.insert(1)
    assert empty_bt.root.val is 1


def test_inserting_a_non_integer(empty_bt):
    """ testing for inserting a none integer
    """
    empty_bt.insert('a')
    assert empty_bt.root.val is 'a'


def test_bt_takes_iterables(small_bt):
    """ Checks for the value of root when iterable is pushed in
    """
    assert small_bt.root.val is 5
    assert small_bt.root.left.val is 2
    assert small_bt.root.right.val is 9


def test_inserting_into_a_small_bt(small_bt):
    """ testing for inserting into bt with nodes
    """
    small_bt.insert(7)
    assert small_bt.root.right.left.val is 7


def test_inserting_value_already_exist(empty_bt):
    """ testing for inserting a value that already exist in the bt
    """
    empty_bt.insert(1)
    empty_bt.insert(1)
    assert empty_bt.root.val is 1
    assert empty_bt.root.left is None
    assert empty_bt.root.right is None


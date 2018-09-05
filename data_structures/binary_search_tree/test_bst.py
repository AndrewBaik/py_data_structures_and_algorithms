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


def test_preorder_traversal(balanced_bt):
    """ testing for pre_order traversal order
    """
    expected = [5, 3, 2, 4, 8, 7, 9]
    actual = []

    def generate_list(node):
        actual.append(node.val)

    balanced_bt.pre_order(generate_list)
    assert expected == actual


def test_inorder_traversal(balanced_bt):
    """ testing for in_order traversal order
    """
    expected = [2, 3, 4, 5, 7, 8, 9]
    actual = []

    def generate_list(node):
        actual.append(node.val)

    balanced_bt.in_order(generate_list)
    assert expected == actual


def test_postorder_traversal(balanced_bt):
    """ testing for post_order traversal order
    """
    expected = [2, 4, 3, 7, 9, 8, 5]
    actual = []

    def generate_list(node):
        actual.append(node.val)

    balanced_bt.post_order(generate_list)
    assert expected == actual


def test_breadth_first_with_unbalanced_bt(balanced_bt):
    """ testing for breadth frist traversal with an unbalanced bt
    """
    balanced_bt.insert(1)
    balanced_bt.insert(10)
    expected = [5, 3, 8, 2, 4, 7, 9, 1, 10]
    actual = []

    def generate_list(node):
        actual.append(node.val)

    balanced_bt.breadth_first(generate_list)
    assert expected == actual


def test_breadth_first_using_bigger_bt(balanced_bt):
    """ testing for breadth first traversal approach with balanced bt
    """
    expected = [5, 3, 8, 2, 4, 7, 9]
    actual = []

    def generate_list(node):
        actual.append(node.val)

    balanced_bt.breadth_first(generate_list)
    assert expected == actual


def test_breadth_first_empty_bt(empty_bt):
    """ testing breadth first with empty bt
    """
    with pytest.raises(ValueError):
        empty_bt.breadth_first()


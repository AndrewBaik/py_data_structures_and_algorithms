from .linked_list import LinkedList
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


def test_linked_list_exist():
    """ Checking for the linked list connection
    """
    assert LinkedList


def test_create_instance_of_list():
    """ checks for linkedlist instance
    """
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_iterable_argument():
    """ testing if linked list takes iterable argument
    """
    lll = LinkedList([1, 2, 3, 4])
    assert lll.includes(1)
    assert lll.includes(2)
    assert lll.includes(3)
    assert lll.includes(4)


def test_default_property_head(empty_list):
    """ testing the linked list attributes
    """
    assert empty_list.head is None


def test_default_property_length(empty_list):
    """ test for the length of linked list
    """
    assert empty_list._length == 0


def test_insertion_successfull(empty_list):
    """ test for insertion method
    """
    assert empty_list.head is None
    empty_list.insert(25)
    assert empty_list.head.val is 25


def test_length_of_list_increases_on_insertion(empty_list):
    """ testing for __len__ method to display the length
    """
    assert len(empty_list) == 0
    empty_list.insert(25)
    assert len(empty_list) == 1


def test_includes_returns_true_if_exists(small_list):
    """ test for includes method to return True when it should
    """
    actual = small_list.includes(4)
    assert actual is True


def test_includes_returns_false_if_nonexists(small_list):
    """ test for includes method to return False when it should
    """
    assert small_list.includes(100) is False
    assert small_list.includes(0) is False


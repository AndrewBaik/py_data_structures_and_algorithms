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


def test_append_new_node_at_the_end(small_list):
    """ test of append method to validate if node is being added at the
        end
    """
    small_list.append(5)
    length = 5
    assert small_list.includes(5)
    assert len(small_list) == length


def test_insert_new_node_before(small_list):
    """ test of inserting a new node before a certain node in the linked list
    """
    small_list.insertBefore(2, 5)
    length = 5
    assert small_list.includes(5)
    assert len(small_list) == length


def test_insert_new_node_after(small_list):
    """ test of inserting a new node after a certain node in the linked list
    """
    small_list.insertAfter(3, 5)
    length = 5
    assert small_list.includes(5)
    assert len(small_list) == length


def test_insert_new_node_after_with_invalid_input(small_list):
    """ test of inserting a new node after a certain node in the linked list
    """
    #with pytest.raises(AssertionError):
    assert small_list.insertAfter(13, 5)


def test_insertion_kth_from_end_when_value_exist_in_ll(small_list):
    """ test for returning the appropriate value when insertion is called
    """
    assert small_list.kth_from_the_end(0) == 1
    assert small_list.kth_from_the_end(1) == 2
    assert small_list.kth_from_the_end(2) == 3
    assert small_list.kth_from_the_end(3) == 4


def test_insertion_kth_from_end_when_value_not_exist_in_ll(small_list):
    """ test for returning the exception/error when input is greater than the length of the linked list
    """
    with pytest.raises(AttributeError):
        small_list.kth_from_the_end(4)

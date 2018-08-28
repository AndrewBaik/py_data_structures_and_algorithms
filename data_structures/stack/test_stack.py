from .stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def small_stack():
    return Stack([4, 3, 2, 1])


def test_stack_exist():
    """ Checking for the stack connection
    """
    assert Stack


def test_instance_of_stack():
    """ tests for data type of stack
    """
    check_stack = Stack()
    assert isinstance(check_stack, Stack)


def test_default_property_top(empty_stack):
    """ testing the stack top attributes
    """
    assert empty_stack.top is None


def test_default_property_length(empty_stack):
    """ test for the length of stack
    """
    assert empty_stack._length == 0


def test_iterable_argument():
    """ testing if stack takes iterable argument
    """
    check_stack = Stack([1, 2, 3, 4])
    assert check_stack._length is 4


def test_length_of_stack_increases_on_insertion(empty_stack):
    """ testing for __len__ method to display the length
    """
    assert len(empty_stack) is 0
    empty_stack.push(25)
    empty_stack.push(20)
    empty_stack.push(15)
    assert len(empty_stack) is 3


def test_for_stack_attributes_when_pushed(empty_stack):
    """ testing for checking the value of top when pushed
    """
    empty_stack.push(5)
    assert empty_stack.top.val is 5


def test_for_stack_pop(small_stack):
    """ test for change in number of Node in stack when pop()
    """
    assert small_stack._length is 4
    small_stack.pop()
    assert small_stack._length is 3


def test_for_top_value_when_pop(small_stack):
    """ test for change in .top reference when pop()
    """
    assert small_stack.top.val is 1
    small_stack.pop()
    assert small_stack.top.val is 2


def test_for_peek(small_stack):
    """ test for peeking the top of a stack
    """
    top = small_stack.peek()
    assert top.val is 1


def test_for_peek_empty_stack(empty_stack):
    """ testing for a peeking an empty stack
    """
    with pytest.raises(AttributeError):
        top = empty_stack.peek()
        top.val

from .queue import Queue
import pytest


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    return Queue([4, 3, 2, 1])


def test_queue_exist():
    """ Checking for the queue connection
    """
    assert Queue


def test_instance_of_queue():
    """ tests for data type of queue
    """
    check_queue = Queue()
    assert isinstance(check_queue, Queue)


def test_default_property_front_rear(empty_queue):
    """ testing the queue front and rear attributes
    """
    assert empty_queue.front is None
    assert empty_queue.rear is None


def test_default_property_length(empty_queue):
    """ test for the length of queue
    """
    assert empty_queue._length == 0


def test_iterable_argument():
    """ testing if queue takes iterable argument
    """
    check_queue = Queue([1, 2, 3, 4])
    assert check_queue._length is 4


def test_length_of_queue_increases_on_insertion(empty_queue):
    """ testing for __len__ method to display the length
    """
    assert len(empty_queue) is 0
    empty_queue.enqueue(25)
    empty_queue.enqueue(20)
    empty_queue.enqueue(15)
    assert len(empty_queue) is 3


def test_for_queue_attributes_when_enqueue(empty_queue):
    """ testing for checking the value of front and rear when enqueue
    """
    empty_queue.enqueue(5)
    assert empty_queue.front.val is 5
    assert empty_queue.rear.val is 5


def test_for_queue_dequeue(small_queue):
    """ test for change in number of Node in queue when dequeue()
    """
    assert small_queue._length is 4
    small_queue.dequeue()
    assert small_queue._length is 3


def test_for_top_value_when_pop(small_queue):
    """ test for change in .rear reference when dequeue()
    """
    assert small_queue.front.val is 4
    small_queue.dequeue()
    assert small_queue.front.val is 3

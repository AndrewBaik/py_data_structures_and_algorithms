from .queue_with_stacks import Queue, Stack
import pytest


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)
    return queue


def test_instance_of_queue():
    """ testing instance of queue
    """
    assert Queue()


def test_instance_of_queue_front_and_rear(small_queue):
    """ testing for front and rear attributes of queue
    """
    assert small_queue.front.val == 4
    assert small_queue.rear.val == 1


def test_attribute_of_two_stacks(empty_queue):
    """ testing for instances of two stacks within the queue
    """
    assert isinstance(empty_queue.stack1, Stack)
    assert isinstance(empty_queue.stack2, Stack)


def test_length_attribute(empty_queue):
    """ testing for length attribute
    """
    assert empty_queue._length == 0


def test_length_after_enqueue(empty_queue):
    """ testing for length of queue after enqueue
    """
    empty_queue.enqueue(5)
    assert empty_queue._length == 1


def test_value_of_enqueued_node(empty_queue):
    """ testing for values of front and rear after enqueue
    """
    empty_queue.enqueue(10)
    assert empty_queue.front.val == 10
    assert empty_queue.rear.val == 10


def test_change_in_rear_value_enqueue(small_queue):
    """ testing for change in rear value by enqueue small queue
    """
    assert small_queue.rear.val is 1
    small_queue.enqueue(5)
    assert small_queue.rear.val is 5


def test_length_after_dequeue(small_queue):
    """ test for change in number of Node in queue when dequeue()
    """
    assert small_queue._length is 4
    small_queue.dequeue()


def test_for_top_value_when_pop(small_queue):
    """ test for change in length after dequeue()
    """
    assert small_queue._length is 4
    small_queue.dequeue()
    assert small_queue._length is 3
    small_queue.dequeue()
    assert small_queue._length is 2


def test_for_dequeue_empty_queue(empty_queue):
    """ test for dequeue a empty queue
    """
    assert empty_queue.dequeue() is None

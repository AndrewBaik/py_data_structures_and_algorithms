from .fifo_animal_shelter import Animal_Shelter
import pytest


@pytest.fixture
def empty_shelter():
    return Animal_Shelter()


@pytest.fixture
def small_shelter():
    shelter = Animal_Shelter()
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    return shelter


def test_animal_shelter_connected():
    """ test for connection with animal shelter
    """
    assert Animal_Shelter()


def test_instance_of_animalshelter_class(empty_shelter):
    """ test the instance of animal shelter with fixture created
    """
    assert isinstance(empty_shelter, Animal_Shelter)


def test_attribute_existance(empty_shelter):
    """ test for attribute values with empty animal shelter
    """
    assert empty_shelter.front is None
    assert empty_shelter.rear is None
    assert empty_shelter._length is 0


def test_enqueue_with_animal(empty_shelter):
    """ test for .front value when enqueued an animal object
    """
    empty_shelter.enqueue('cat')
    assert empty_shelter.front.val == 'cat'


def test_enqueue_front_rear(small_shelter):
    """ test for values of front and rear small shelter
    """
    assert small_shelter.front.val is 'cat'
    assert small_shelter.rear.val is 'dog'


def test_enqueue_length(empty_shelter):
    """ test for length of animal shelter after enqueue object
    """
    assert empty_shelter._length is 0
    empty_shelter.enqueue('dog')
    assert empty_shelter._length is 1


def test_dequeue_length(small_shelter):
    """ test for length of animal shelter after dequeue animal object
    """
    assert small_shelter._length is 6
    small_shelter.dequeue()
    assert small_shelter._length is 5


def test_dequeue_empty_shelter(empty_shelter):
    """ test for return None when dequeue empty shelter
    """
    assert empty_shelter.dequeue() is None


def test_remove_specified_animal(empty_shelter):
    """ test for dequeue specific animal from short shelter
    """
    empty_shelter.enqueue('dog')
    empty_shelter.dequeue('dog')
    assert empty_shelter.front is None
    assert empty_shelter.rear is None


def test_dequeue_selected_animal(empty_shelter):
    """ test for dequeue second on the list
    """
    empty_shelter.enqueue('cat')
    empty_shelter.enqueue('dog')
    empty_shelter.enqueue('cat')

    empty_shelter.dequeue('dog')
    assert empty_shelter.rear.val is 'cat'
    assert empty_shelter.rear._next.val is 'cat'


def test_dequeue_nonexisting_animal(empty_shelter):
    """ test for dequeueing an none existing animal from short list
    """
    empty_shelter.enqueue('dog')
    empty_shelter.enqueue('dog')
    empty_shelter.enqueue('dog')
    empty_shelter.enqueue('dog')
    empty_shelter.enqueue('dog')
    empty_shelter.enqueue('dog')
    assert empty_shelter.dequeue('cat') is None

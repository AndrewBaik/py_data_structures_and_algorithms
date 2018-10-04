from .radix_sort import radix_sort
from random import shuffle
import pytest


def test_radix_sort():
    """ test returning correct sorted list
    """
    expected = [num for num in range(5, 15)]
    unsorted = expected[:]
    shuffle(unsorted)
    now_sorted = radix_sort(unsorted)
    assert expected == now_sorted


def test_radix_sort_sorted():
    """ test sorting already sorted list
    """
    expected = [num for num in range(9999)]
    now_sorted = radix_sort(expected)
    assert expected == now_sorted


def test_radix_sort_duplicates():
    """ test sorting duplicate values
    """
    unsorted = [25, 285, 9781, 142, 5, 663, 4132, 76, 3332, 705]
    expect = [5, 25, 76, 142, 285, 663, 705, 3332, 4132, 9781]
    assert expect == radix_sort(unsorted)


def test_radix_sort_none_list():
    """ test receiving anything other than a list
    """
    with pytest.raises(TypeError):
        radix_sort('hello world')

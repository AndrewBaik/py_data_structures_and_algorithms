from .quick_sort import quick_sort
from random import shuffle
import pytest


def test_quick_sort():
    """ test returning correct sorted list
    """
    expected = [num for num in range(20)]
    unsorted = expected[:]
    shuffle(unsorted)
    now_sorted = quick_sort(unsorted)
    assert expected == now_sorted


def test_quick_sort_sorted():
    """ test sorting already sorted list
    """
    expected = [num for num in range(20)]
    now_sorted = quick_sort(expected)
    assert expected == now_sorted


def test_quick_sort_duplicates():
    """ test sorting duplicate values
    """
    unsorted = [5, 2, 9, 1, 3, 6, 2, 5, 1, 7]
    expect = [1, 1, 2, 2, 3, 5, 5, 6, 7, 9]
    assert expect == quick_sort(unsorted)


def test_quick_sort_none_list():
    """ test receiving anything other than a list
    """
    with pytest.raises(TypeError):
        quick_sort('hello world')

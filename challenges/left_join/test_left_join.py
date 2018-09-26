from py_data_structures_and_algorithms.data_structures.hashtable.hash_table import HashTable
from .left_join import left_join
import pytest


@pytest.fixture
def ht1():
    ht = HashTable()
    ht.set('A', '1')
    ht.set('B', '2')
    ht.set('C', '3')
    ht.set('D', '4')
    ht.set('E', '5')
    return ht


@pytest.fixture
def ht2():
    ht = HashTable()
    ht.set('A', '9')
    ht.set('C', '8')
    ht.set('E', '7')
    ht.set('G', '6')
    ht.set('I', '5')
    return ht


@pytest.fixture
def ht3():
    ht = HashTable()
    ht.set('B', '10')
    ht.set('D', '20')
    ht.set('F', '30')
    ht.set('H', '40')
    return ht


def test_return_joint_list(ht1, ht2):
    """ test for correct list of values
    """
    expect = [
        [65, '1', '9'],
        [66, '2', 'NULL'],
        [67, '3', '8'],
        [68, '4', 'NULL'],
        [69, '5', '7'],
    ]
    actual = left_join(ht1, ht2)
    assert actual == expect


def test_return_joint_list_2(ht1, ht3):
    """ test for corret list of values 2
    """
    expect = [
        [65, '1', 'NULL'],
        [66, '2', '10'],
        [67, '3', 'NULL'],
        [68, '4', '20'],
        [69, '5', 'NULL'],
    ]
    actual = left_join(ht1, ht3)
    assert actual == expect


def test_return_empty_list(ht1):
    """ test for push in empty hashtable and return empty list
    """
    ht = HashTable()
    actual = left_join(ht, ht1)
    assert actual == []

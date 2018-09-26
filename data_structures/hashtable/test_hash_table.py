from .hash_table import HashTable
import pytest


@pytest.fixture
def empty_ht():
    return HashTable()


@pytest.fixture
def small_ht():
    ht = HashTable()
    ht.set('A', '1')
    ht.set('A', '2')
    ht.set('B', '1')
    ht.set('B', '2')
    ht.set('C', '1')
    ht.set('C', '2')
    return ht


def test_is_instance_hashtable(empty_ht):
    """ test for instance of hashtable
    """
    assert isinstance(empty_ht, HashTable)


def test_ht_properties(empty_ht):
    """ test for hashtable value
    """
    assert empty_ht.hashtable == []


def test_hasing(empty_ht):
    """ test for hashing value
    """
    ht = HashTable()
    test = ht._hash_key('hello world')
    assert test == empty_ht._hash_key('hello world')


def test_hashtable_set(empty_ht):
    """ test for setting value to hashtble
    """
    empty_ht.set('A', '1')
    ll = empty_ht.hashtable[0]
    assert ll.head._next.val == '1'


def test_hashtable_objects(small_ht):
    """ test saved linked list objects
    """
    hashed1 = small_ht._hash_key('A')
    hashed2 = small_ht._hash_key('B')
    hashed3 = small_ht._hash_key('C')
    ll1 = small_ht.hashtable[0]
    ll2 = small_ht.hashtable[1]
    ll3 = small_ht.hashtable[2]
    assert hashed1 == ll1.head.val
    assert hashed2 == ll2.head.val
    assert hashed3 == ll3.head.val


def test_hashtable_get(small_ht):
    """ test for getting a list of values
    """
    expected = ['1', '2']
    actual = small_ht.get('A')
    assert expected == actual


def test_hashtable_get_more(small_ht):
    """ test of getting a long list of values
    """
    small_ht.set('C', '5')
    small_ht.set('C', '15')
    small_ht.set('C', '9')
    small_ht.set('C', '16')
    small_ht.set('C', '4')
    small_ht.set('C', '65')
    small_ht.set('C', '222')
    expect = ['1', '2', '5', '15', '9', '16', '4', '65', '222']
    actual = small_ht.get('C')
    assert expect == actual


def test_hashtable_get_notexist(small_ht):
    """ test for getting a list with key dont exist
    """
    expected = []
    actual = small_ht.get('Z')
    assert expected == actual


def test_hashtable_remove(small_ht):
    """ test for removing values
    """
    expect = []
    small_ht.remove('A')
    assert expect == small_ht.get('A')

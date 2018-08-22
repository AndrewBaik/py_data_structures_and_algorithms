from .ll_merge import merge, LinkedList


def test_merge_two_equal_sized_linkedlist():
    """ testing for the merge function to accept and zip two equal sized linked list
    """
    ll1 = LinkedList([1, 3, 5, 7])
    ll2 = LinkedList([2, 4, 6, 8])
    output = merge(ll1, ll2)
    assert len(output) == 8


def test_merge_first_linkedlist_is_longer():
    """ testing for the merge function to accept and zip when first linkedlist is longer than second
    """
    ll1 = LinkedList([1, 3, 5, 7, 9, 10])
    ll2 = LinkedList([2, 4, 6, 8])
    output = merge(ll1, ll2)
    assert len(output) == 10


def test_merge_second_linkedlist_is_longer():
    """ testing for the merge function to accept and zip when second linkedlist is longer than second
    """
    ll1 = LinkedList([1, 3, 5, 7])
    ll2 = LinkedList([2, 4, 6, 8, 9, 10, 11, 12])
    output = merge(ll1, ll2)
    assert len(output) == 12


def test_merge_when_one_list_is_empty():
    """ testing for merge function when one list is empty
    """
    ll1 = LinkedList()
    ll2 = LinkedList([1, 2, 3, 4, 5, 6])
    output = merge(ll1, ll2)
    assert len(output) == 6

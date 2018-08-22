from py_data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList


def merge(ll1, ll2):
    """ merges two linked list into one
    """
    output = LinkedList()
    current1 = ll1.head
    current2 = ll2.head
    while current1 is not None or current2 is not None:
        if current1 is not None:
            output.append(current1.val)
            current1 = current1._next
        if current2 is not None:
            output.append(current2.val)
            current2 = current2._next
    return output


if __name__ == '__main__':
    ll = LinkedList([1, 3, 5, 7])
    ll2 = LinkedList([2, 4, 6, 8])
    ll3 = merge(ll, ll2)
    current = ll3.head
    while current is not None:
        print(str(current.val))
        current = current._next

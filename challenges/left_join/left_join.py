from py_data_structures_and_algorithms.data_structures.hashtable.hash_table import HashTable


def left_join(ht1, ht2):
    """
    """
    output = []

    for ll in ht1.hashtable:
        new_list = []
        new_list.append(ll.head.val)
        new_list.append(ll.head._next.val)
        new_list.append('NULL')
        output.append(new_list)

    for ll in ht2.hashtable:
        for a_list in output:
            if a_list[0] == ll.head.val:
                index = output.index(a_list)
                a_list[2] = ll.head._next.val
                output[index] = a_list
    return output

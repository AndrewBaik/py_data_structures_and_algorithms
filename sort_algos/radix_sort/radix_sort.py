from py_data_structures_and_algorithms.data_structures.queue.queue import Queue


def radix_sort(unsorted_list):
    """ Radix sort algorithm with unsorted list of elements
    """
    buckets = [Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue()]
    stop = False
    counter = 10

    while not stop:
        stop = True

        for value in unsorted_list:
            value_validation = value % counter
            bucket_index = value_validation // (counter // 10)
            queue = buckets[bucket_index]
            queue.enqueue(value)

            if value_validation is not value:
                stop = False

        index_counter = 0
        for index in range(10):
            q = buckets[index]
            while q.front is not None:
                node = q.dequeue()
                unsorted_list[index_counter] = node.val
                index_counter += 1
        counter *= 10

    return unsorted_list



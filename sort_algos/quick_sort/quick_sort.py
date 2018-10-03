def quick_sort(a_list):
    """ Quick sort algorithm with unsorted list of elements
    """
    for index in range(len(a_list)):
        pivot = index
        store_index = pivot + 1
        for runner in range(pivot + 1, len(a_list)):
            if a_list[runner] < a_list[pivot]:
                a_list[runner], a_list[store_index] = a_list[store_index], a_list[runner]
                store_index += 1
        a_list[pivot], a_list[store_index - 1] = a_list[store_index - 1], a_list[pivot]
        if pivot + 1 is not store_index:
            for recheck in range(pivot, store_index):
                if a_list[recheck] < a_list[pivot]:
                    a_list[pivot], a_list[recheck] = a_list[recheck], a_list[pivot]
    return a_list

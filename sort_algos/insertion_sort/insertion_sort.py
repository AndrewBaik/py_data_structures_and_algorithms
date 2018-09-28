
def insertion_sort(unsorted):
    """
    """
    for i in range(1, len(unsorted)):
        current = unsorted[i]
        position = i
        while current < unsorted[position - 1] and position > 0:
            unsorted[position], unsorted[position - 1] = unsorted[position - 1], unsorted[position]
            position -= 1
    return unsorted

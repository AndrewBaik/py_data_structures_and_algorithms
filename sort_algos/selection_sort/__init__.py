def selection_sort(unsorted):
    """ Takes a unsorted list, using selection sorting method, where validates integers in each indeces and compare to others.
        returns a list of sorted list.
    """
    for i in range(len(unsorted)):
        min_val = i
        for runner in range(i + 1, len(unsorted)):
            if unsorted[runner] < unsorted[min_val]:
                min_val = runner
        unsorted[i], unsorted[min_val] = unsorted[min_val], unsorted[i]
    return unsorted

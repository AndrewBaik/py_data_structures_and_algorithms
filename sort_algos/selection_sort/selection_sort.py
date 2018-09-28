
def selection_sort(unsorted):
    """ takes a list of unsorted values, using selection sort method, returns sorted list of values
    """
    if type(unsorted) is not list:
        raise TypeError('input argument must be list')

    for i in range(len(unsorted)):
        min_val = i

        for runner in range(i + 1, len(unsorted)):
            if unsorted[runner] < unsorted[min_val]:
                min_val = runner
        unsorted[i], unsorted[min_val] = unsorted[min_val], unsorted[i]
    return unsorted

def merge_sort(usr_input):
    """ Given unsorted list, sortings a list of given values using merge sort algorithm
    """
    def _walk(input_list):
        """ Recursion method to parse the length of list
        """
        output = []
        maxim = len(input_list)
        minim = 0
        mid = (maxim + minim) // 2

        if maxim - minim > 2:
            list_left = input_list[:mid]
            list_right = input_list[mid:]
            left_list = _walk(list_left)
            right_list = _walk(list_right)

            left = 0
            right = 0
            while left < len(left_list) or right < len(right_list):
                if len(left_list) == left:
                    output.append(right_list[right])
                    right += 1
                elif len(right_list) == right:
                    output.append(left_list[left])
                    left += 1
                elif left_list[left] > right_list[right]:
                    output.append(right_list[right])
                    right += 1
                else:
                    output.append(left_list[left])
                    left += 1
            return output

        if len(input_list) is 2:
            if input_list[0] > input_list[1]:
                input_list[0], input_list[1] = input_list[1], input_list[0]

        return input_list
    output = _walk(usr_input)
    return output

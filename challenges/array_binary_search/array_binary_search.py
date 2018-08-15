def binary_search(input_list, input_value):
    min = 0
    max = len(input_list) - 1
    mid = calculate_mid(min, max)
    while min <= max:
        if input_list[mid] == input_value:
            return mid
        if input_list[mid] < input_value:
            min = mid + 1
            mid = calculate_mid(mid, max)
        elif input_list[mid] > input_value:
            max = mid - 1
            mid = calculate_mid(min, mid)
    return -1


def calculate_mid(low, high):
    mid = (high + low) // 2
    return mid


def execute():
    a = input().split()
    b = input()
    c = binary_search(a, b)
    print(c)

if __name__ == '__main__':
    execute()

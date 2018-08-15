from .array_binary_search import binary_search


def test_binary_search_exist_even_low():
    expect = 2
    actual = binary_search([4, 8, 15, 16, 23, 42], 15)
    assert expect == actual


def test_binary_search_exist_even_high():
    expect = 4
    actual = binary_search([4, 8, 15, 16, 23, 42], 23)
    assert expect == actual


def test_binary_search_exist_odd_low():
    expect = 1
    actual = binary_search([4, 8, 15, 16, 23, 42, 68], 8)
    assert expect == actual


def test_binary_search_exist_odd_high():
    expect = 5
    actual = binary_search([4, 8, 15, 16, 23, 42, 68], 42)
    assert expect == actual


def test_binary_search_nonexist():
    expect = -1
    actual = binary_search([11, 22, 33, 44, 55, 66], 30)
    assert expect == actual


def test_binary_search_empty_list():
    expect = -1
    actual = binary_search([], 1)
    assert expect == actual

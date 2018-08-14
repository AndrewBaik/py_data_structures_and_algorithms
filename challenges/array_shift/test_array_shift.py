from .array_shift import insertShiftArray
import pytest


def test_check_for_shifted_list_on_even_number_length():
    expected = [2, 4, 5, 6, 8]
    actual = insertShiftArray([2, 4, 6, 8], 5)
    assert expected == actual


def test_check_for_shifted_list_on_old_number_length():
    expected = [4, 8, 15, 16, 23, 42]
    actual = insertShiftArray([4, 8, 15, 23, 42], 16)
    assert expected == actual


def test_check_for_shifted_list_with_string_elements():
    expected = ['a', 'b', 'c', 'd', 'e']
    actual = insertShiftArray(['a', 'b', 'd', 'e'], 'c')
    assert expected == actual


def test_check_for_shifted_list_with_dictionary():
    with pytest.raises(KeyError):
        insertShiftArray({'one': 'two'}, 'three')

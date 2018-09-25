from .repeated_words import repeated_words
import pytest


def test_return_a_word():
    """ test for returing the correct word
    """
    given = 'another a willing to a long lake'
    expect = 'a'
    actual = repeated_words(given)
    assert expect == actual


def test_return_capitalization():
    """ test for returning the correct word with capitalization
    """
    given = 'Willing to given a willing for you'
    expect = 'willing'
    actual = repeated_words(given)
    assert expect == actual


def test_return_special_symbol():
    """ test for returning repeating special symbol
    """
    given = 'dollar sign is $ and people love $ its never enough'
    expect = '$'
    actual = repeated_words(given)
    assert expect == actual


def test_return_with_no_repeated():
    """ test when given has no repeated word
    """
    given = 'there are no repeated words'
    with pytest.raises(AttributeError):
        repeated_words(given)



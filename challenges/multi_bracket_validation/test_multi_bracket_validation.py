from .multi_bracket_validation import multi_bracket_validation


def test_simple_balance_string():
    """ given simple paired bracket, expect true
    """
    assert multi_bracket_validation('()') is True


def test_with_only_open_bracket():
    """ given string of only open brackets, expect false
    """
    assert multi_bracket_validation('({[') is False


def test_with_only_close_bracket():
    """ given string of only closed brackets, expect false
    """
    assert multi_bracket_validation('])}') is False


def test_given_string_of_brackets():
    """ given string of paired brackets, exptect true
    """
    string = '({[]})'
    assert multi_bracket_validation(string) is True


def test_giving_string_with_letters():
    """ given balanced string of brackets with none bracket characters, expect true
    """
    string = '[co]d{e} f(el)l[ows]'
    assert multi_bracket_validation(string) is True


def test_given_close_first():
    """ given balanced brackets with wrong order, expect false
    """
    string = ']['
    assert multi_bracket_validation(string) is False


def test_given_edge_string():
    """ given edge case of string thats paired, but out of order
    """
    string = '([){]}'
    assert multi_bracket_validation(string) is False


def test_given_none_bracket_string():
    """ given none bracket string, exptect true
    """
    string = 'COde fellows'
    assert multi_bracket_validation(string) is True

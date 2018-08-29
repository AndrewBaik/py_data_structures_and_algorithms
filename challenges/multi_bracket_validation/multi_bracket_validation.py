from ..fifo_animal_shelter.node import Node
from py_data_structures_and_algorithms.data_structures.stack.stack import Stack


def multi_bracket_validation(input):
    """ takes an argument of a string and validates if all brackets are paired
    """
    stack = Stack()
    input_list = input.replace('', ' ').split()
    for char in input_list:
        if char is '(' or char is '{' or char is '[':
            stack.push(char)
        elif char is ')' or char is '}' or char is ']':
            if stack.top is not None:
                if char is ')' and stack.top.val is '(':
                    stack.pop()
                elif char is ']' and stack.top.val is '[':
                    stack.pop()
                elif char is '}' and stack.top.val is '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
    if stack.top is None:
        return True
    return False

# -*- coding: UTF-8 -*-
from substring import find_substring
from pytest import mark

"""
Execution from command prompt or terminal example:
~$ py.test test.py
"""


@mark.parametrize("string, substring",
                  [(None, None),
                   ("string", "substring"),
                   ("", "substring"),
                   ("string", ""),
                   ("ĄČĘĖĮŠŲŪ()_Ž", "ĄČĘ")])
def test_function_pass(string, substring):
    """
    Parametrized test function for find_substring(string, substring) function.
    This functions must be run with py.test testing framework to work correctly.
    Function runs find_substring(string, substring) correctly ergo passes the test.

    :param string: longer string line in which search of the substring will be performed.
    :param substring: shorter fragment of string which may or may not be in the longer string.
    :return: None.
    """
    assert find_substring(string, substring) == False


@mark.parametrize("string, substring",
                  [(None, None),
                   ("string", "substring"),
                   ("", "substring"), ("string", ""),
                   ("1234567890-=_+[]';#/.,<>||", ">|")])
def test_function_fail(string, substring):
    """
    Parametrized test function for find_substring(string, substring) function.
    This functions must be run with py.test testing framework to work correctly.
    Function runs find_substring(string, substring) incorrectly ergo fails the test.

    :param string: longer string line in which search of the substring will be performed.
    :param substring: shorter fragment of string which may or may not be in the longer string.
    :return: None.
    """
    assert find_substring(string, substring) == True


# -*- coding: UTF-8 -*-
from __future__ import print_function

"""
File contains program that requests string input from user and checks
if a user specified substring exists in that string.
Execution from command prompt or terminal example:
~$ python substring.py
"""


def instructions():
    """
    Function displays instructions for the user.

    :return: None
    """

    print("+--------------------------------------+\n"
          "|    Instructions                      |\n"
          "+--------------------------------------+\n"
          "| 1 to enter new string                |\n"
          "| 2 to enter new substring             |\n"
          "| 3 to check if substring is in string |\n"
          "| 4 to display string and substring    |\n"
          "| 5 to exit                            |\n"
          "+--------------------------------------+\n")


def get_user_choice():
    """
    Function returns user's input as an integer.

    :return: user's input as an integer.
    """

    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Input exception: Incorrect input!")
        return None
    except SyntaxError:
        print("Input exception: Unrecognized character!")
        return None


def get_user_input(prompt):
    """
    Function returns user's input as a string.

    :type prompt: str
    :param prompt: prompt message to specify information needed.
    :return: user's input as a sting.
    """

    try:
        return str(raw_input(prompt))
    except ValueError:
        print("Input exception: Incorrect input!")
        return None
    except SyntaxError:
        print("Input exception: Unrecognized character!")
        return None


def find_substring(string, substring):
    """
    Function performs a search of the substring specified in string parameter.

    :type string: str
    :param string: longer string line in which search of the substring will be performed.
    :type substring: str
    :param substring: shorter fragment of string which may or may not be in the longer string.
    :return: True if substring is part of a string and visa versa if not.
    """

    if string is None or substring is None:
        return False
    if len(substring) <= 0 or len(string) <= 0:
        return False
    if len(substring) > len(string):
        return False
    else:
        for i in range(len(string) - len(substring) + 1):
            if string[i] == substring[0] and len(substring) == 1:
                return True
            if string[i] == substring[0]:
                for n in range(1, len(substring)):
                    if string[i+n] != substring[n]:
                        break
                    if n == len(substring) - 1:
                        return True
        return False


def main():
    """
    The entry point of the program launches main cycle.

    :return: None
    """

    print("This program finds substring in string")
    string = None
    substring = None
    instructions()
    while True:
        choice = get_user_choice()
        if choice == 1:
            string = get_user_input("Enter your string: ")
        elif choice == 2:
            substring = get_user_input("Enter your substring: ")
        elif choice == 3:
            print("Looking substring \"%s\" in string \"%s\"" % (substring, string))
            print(find_substring(string, substring))
        elif choice == 4:
            print("Your string: \"%s\"" % string)
            print("your substring: \"%s\"" % substring)
        elif choice == 5:
            break
        else:
            print("Error: No such choice!")
            instructions()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on: June 2021
# this program determines whether or not a string is a palindrome

import math


def find_palindrome(string):
    # this function determines if the string is a palindrome or not
    # Source used to determine palindrome in python:
    # https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/

    string_divide = len(string)/2
    for character_count in range(0, int(string_divide)):
        if string[character_count] != string[len(string)-character_count-1]:
            return False
    return True


def main():
    # this function collects the string, then shows if it is a palindrome
    #     or not to the user

    # input
    print("Is it a palindrome?")
    print("If you use letters, make sure they are all"
          " either lower or upper cased.")
    string_input = input("\nPlease enter a string: ")

    # call function(s)
    palindrome_or_not = find_palindrome(string_input)

    # output
    if (palindrome_or_not):
        print("\n{} is a palindrome!".format(string_input))
    else:
        print("\n{} is not a palindrome!".format(string_input))
    print("\nThanks for participating!")


if __name__ == "__main__":
    main()

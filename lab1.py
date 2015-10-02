#!/usr/bin/env python3

""" Graded Lab #1 for Inf1340, Fall 2015 """

__author__ = 'Ming Fu'
__email__ = "mm.fu@mail.utoronto.ca"


def vowel_or_consonant():
    """
    Exercise: Vowel or Consonant
    Reads a letter of the alphabet from the user. (You can assume that it's
    lowercase.) If the user enters a, e, i, o or u then your program should
    display "vowel". If the user enters y then your program should display
    "sometimes a vowel, sometimes a consonant". Otherwise your program should
    display a message indicating that the letter is a "consonant".
    """
    letter = raw_input("Enter:")
    item1 = "a"
    item2 = "e"
    item3 = "i"
    item4 = "o"
    item5 = "u"
    item6 = "y"

    if letter == item6:
        print("sometimes a vowel, sometimes a consonant")
    elif letter == item1 or letter == item2 or letter == item3 or letter == item4 or letter == item5:
        print("vowel")
    else:
        print("consonant")

# vowel_or_consonant()
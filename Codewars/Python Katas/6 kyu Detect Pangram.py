"""
Description:

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""

# Solution
import string

def is_pangram(s):
    alphabet = string.ascii_lowercase
    
    for i in alphabet:
        if i not in s.lower():
            return False
    else:
        return True


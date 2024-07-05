"""
Description:

Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.
"""


# Solution
def reverse_alternate(string):
  #your code here
    lst = string.split()
    lst_len = len(lst)
    return ' '.join([lst[n][::-1] if n % 2 != 0 else lst[n] for n in range(lst_len)]).strip()

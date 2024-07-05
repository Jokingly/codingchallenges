"""
Description:

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

"""

# Revised Solution
def get_count(sentence):
    return sum(1 for l in sentence if l in 'aeiou')


# First Solution
def get_count(sentence):
    c = 0
    
    for l in sentence:
        if l in 'aeiou':
            c += 1
            
    return c



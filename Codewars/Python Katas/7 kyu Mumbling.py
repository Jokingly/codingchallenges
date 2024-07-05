"""
Description:

This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.

"""

# Revised solution
def accum(s):
    # your code
    return '-'.join(l.upper() + l.lower() * n for n, l in enumerate(s))


# First Solution
def accum(s):
    # your code
    n = 1
    str = ''
    for l in s:
        str += (l * n).title() + '-'
        n += 1
        
    return str[:-1]



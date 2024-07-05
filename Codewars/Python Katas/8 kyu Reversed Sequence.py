"""
Description:

Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]

"""

# Revised Solution
def reverse_seq(n):
    return list(range(n, 0, -1))


# First Solution
def reverse_seq(n):
    return sorted(list(range(1, n + 1)), reverse=True)



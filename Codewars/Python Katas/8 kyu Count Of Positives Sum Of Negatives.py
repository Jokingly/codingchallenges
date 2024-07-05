"""
Description:

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.
Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

"""

# Solution
def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    else:
        pos = len([n for n in arr if n > 0])
        neg = sum([n for n in arr if n < 0])
        return [pos, neg]


"""
Description:

Task

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
Examples

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


"""

# Solution
def sort_array(source_array):
    # Return a sorted array.
    odd_values = sorted([y for y in source_array if y % 2])
    odd_values_indexes = sorted([x for x, y in enumerate(source_array) if y % 2])

    for i in range(len(odd_values)):
        source_array[odd_values_indexes[i]] = odd_values[i]

    return source_array

"""
Description:

Please write a function that sums a list, but ignores any duplicated items in the list.

For instance, for the list [3, 4, 3, 6] the function should return 10,
and for the list [1, 10, 3, 10, 10] the function should return 4.

"""

# Solution
def sum_no_duplicates(l):
    count_dict = {num:l.count(num) for num in l}
    sum_non_dupe_nums = sum([x for x, y in count_dict.items() if y == 1])
    return sum_non_dupe_nums

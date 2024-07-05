"""
Description:

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

"""

# Solution
def move_zeros(lst):
    for i in range(lst.count(0)):
        x = lst.pop(lst.index(0))
        lst.append(x)
    return lst

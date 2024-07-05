"""
Description:

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

uniqueInOrder('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
uniqueInOrder('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
uniqueInOrder([1,2,2,3,3])       == [1,2,3]

"""

# Revised Solution
def unique_in_order(iterable):
    output = []
    
    for i in iterable:
        if len(output) == 0 or i != output[-1]:
            output.append(i)
    
    return output
            


# First Solution
def unique_in_order(iterable):
    
    if len(iterable) == 0:
        return []
    
    output = []
    
    for n in range(len(iterable)):
        if n <= len(iterable)-2:
            if iterable[n] != iterable[n+1]:
                output.append(iterable[n])
    
    output.append(iterable[-1])
            
    return output



"""
Description:

Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]

And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]

"""

# Revised Solution
def tower_builder(n_floors):
    tower = []
        
    for n in range(1, n_floors + 1):
            building = '*' * (2 * n - 1)
            space = ' ' * (n_floors - n)
            
            tower.append(space + building + space)
    
    return tower


# First Solution
def tower_builder(n_floors):
    tower = []
        
    for n in range(n_floors):
            building = '*' + '**' * n
            space_workings = ((n_floors * 2) - 1) - len(building)
            space = int(space_workings / 2) * ' '
            
            tower.append(space + building + space)
    
    return tower



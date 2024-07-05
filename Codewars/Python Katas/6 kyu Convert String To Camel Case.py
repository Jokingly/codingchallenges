"""
Description:

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

"""

# Revised Solution
def to_camel_case(text):
    #your code here
    list = text.replace('-', ' ').replace('_', ' ').split(' ')

    return list[0] + ''.join([word.title() for word in list[1:]])


# First Solution
def to_camel_case(text):
    #your code here
    list = text.replace('-', ' ').replace('_', ' ').split(' ')
    
    if list[0].istitle():
        return ''.join([word.title() for word in list])
    
    else:
        return list[0] + ''.join([word.title() for word in list[1:]])



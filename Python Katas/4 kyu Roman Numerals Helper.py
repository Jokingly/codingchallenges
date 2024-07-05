"""
Description:

Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

    1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
    2008 is written as 2000=MM, 8=VIII; or MMVIII
    1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
Examples

to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1

Help

+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+


"""

# Revised Solution
class RomanNumerals:

    roman_dict = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    def to_roman(val):

        output = ''

        for k, v in RomanNumerals.roman_dict.items():
            while val >= v:
                output += k
                val -= v

        return output

    def from_roman(roman_num):

        output = 0

        for k, v in RomanNumerals.roman_dict.items():
            while roman_num.startswith(k):
                output += v
                roman_num = roman_num[len(k):]

        return output


# First Solution
class RomanNumerals:
    to_roman_dict = {
                    0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',  
                    10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 
                    100: 'C',  200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 
                    1000: 'M', 2000: 'MM', 3000: 'MMM', 4000: '_I_V'
                    }

    def to_roman(val):

        thousands = ''
        hundreds = ''
        tens = ''
        units = ''

        for c, v in enumerate([n for n in str(val)[::-1]]):
            if c == 0:
                units += RomanNumerals.to_roman_dict[int(v)]
            elif c == 1:
                tens += RomanNumerals.to_roman_dict[(10 ** c) * int(v)]
            elif c == 2:
                hundreds += RomanNumerals.to_roman_dict[(10 ** c) * int(v)]
            elif c == 3:
                thousands += RomanNumerals.to_roman_dict[(10 ** c) * int(v)]
        
        to_roman_output = thousands + hundreds + tens + units

        print(f'{val} is {to_roman_output}')
        return to_roman_output

    def from_roman(roman_num):
        input_val = roman_num
        from_roman_output = 0
        from_roman_dict = {
                            'I': 1, 'II': 2, 'III': 3, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 
                            'X': 10, 'XX': 20, 'XXX': 30, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 
                            'C': 100, 'CC': 200, 'CCC': 300, 'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800,  
                            'M': 1000, 'MM': 2000, 'MMM': 3000
                            }
        
        reverse_roman_values = sorted([v for v in from_roman_dict.values()], reverse=True)
        reverse_roman_keys = [list(from_roman_dict.keys())[list(from_roman_dict.values()).index(v)] for v in reverse_roman_values]
        from_roman_aesthetic_nums = ['_I_V', 'CM', 'CD', 'XC', 'XL', 'IX', 'IV']

        for i in from_roman_aesthetic_nums:
            if i in input_val:
                from_roman_output += {y: x for x, y in RomanNumerals.to_roman_dict.items()}[i]
                input_val = input_val.replace(i,'')

        for i in reverse_roman_keys:
            if i in input_val:
                from_roman_output += {y: x for x, y in RomanNumerals.to_roman_dict.items()}[i]
                input_val = input_val.replace(i,'')

        print(f'{roman_num} is {from_roman_output}')
        return from_roman_output



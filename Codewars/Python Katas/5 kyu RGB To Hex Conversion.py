"""
Description:

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
Examples (input --> output):

255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"


"""

# Revised Solution
def rgb(r, g, b):
    
    round = lambda x: min(255, max(x, 0))    

    return ('{:02X}'*3).format(round(r), round(g), round(b))


# First Solution
def rgb(r, g, b):
    rgb_hex = {
        15: "F",
        14: "E",
        13: "D",
        12: "C",
        11: "B",
        10: "A",
        9: "9",
        8: "8",
        7: "7",
        6: "6",
        5: "5",
        4: "4",
        3: "3",
        2: "2",
        1: "1",
        0: "0"
    }
    
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    
    one = rgb_hex[r // 16] + rgb_hex[r % 16]
    two = rgb_hex[g // 16] + rgb_hex[g % 16]
    three = rgb_hex[b // 16] + rgb_hex[b % 16]

    output = one + two + three

    return output



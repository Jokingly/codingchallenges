=begin
Description:

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html
Examples
N 	Product 	N factorial 	Trailing zeros
6 	1*2*3*4*5*6 	720 	1
12 	1*2*3*4*5*6*7*8*9*10*11*12 	479001600 	2

Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

=end

# Solution
def zeros(n)
  if n < 5 
    return 0
  end
  
  (n / 5) + zeros(n / 5)
  
end

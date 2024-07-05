=begin
Description:

In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
--the order is: uppercase letters, lowercase, numbers and special characters.

More examples in the test cases.

Good luck!

=end

# Revised solution
def solve s
    [s.count("A-Z"), s.count("a-z"), s.count("0-9"), s.count("^A-Za-z0-9")]
   end


# First Solution
def solve s
    #..
     out = []
     
     out.push(s.count("A-Z"))
     out.push(s.count("a-z"))
     out.push(s.count("0-9"))
     out.push(s.length - out[0] - out[1] - out[2])
     
     return out
     
   end



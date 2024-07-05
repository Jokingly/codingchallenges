=begin
Description:

The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

For example:

1.08 --> 30

Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

=end

# Revised solution
def cockroach_speed(s)
    # Good Luck!
    ((s * 100000) / (60 * 60)).floor
    
    
  end


# First Solution
def paperwork(n, m)
    #Happy Coding! ^_^
    
    n < 0 || m < 0 ? 0 : n * m
    
  end



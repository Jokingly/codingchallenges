=begin
Description:

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

=end

# Revised solution
def find_short(s)
    s.split.map(&:length).min
end

# First Solution
def find_short(s)
    # your code here
    l = s.split[0].length
    s.split.each { |word| l = word.length if word.length < l }
    return l # l: length of the shortest word
end


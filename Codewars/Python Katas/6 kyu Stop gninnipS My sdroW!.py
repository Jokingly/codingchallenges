"""
Description:

Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"


"""

# Revised solution
def spin_words(sentence):
    # Your code goes here
    return ' '.join([w[::-1] if len(w) >= 5 else w for w in sentence.split()])


# First Solution
def spin_words(sentence):
    # Your code goes here
    output = []
    
    for word in sentence.split(): 
        
        if len(word) >= 5:
            rev_word = ''
            for i in word[::-1]:
                rev_word += i
            output.append(rev_word)
        
        else:
            output.append(word)
    
    return ' '.join(output)



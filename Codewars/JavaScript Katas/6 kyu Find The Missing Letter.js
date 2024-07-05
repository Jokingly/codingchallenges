/*
Description:

Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'

(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!

*/

// Revised solution
function findMissingLetter(array)
{
  // Convert letters into ASCII codes, to be counted,
  // to determine missing letter
  for (i = 0; i < array.length; i++) {
    
    // Variable with what subsequent number should be (current number + 1)
    const subsequentNumberCheck = array[i].charCodeAt(0) + 1;
    // Variable with actual subsequent number
    const subsequentNumber = array[i+1].charCodeAt(0);
    
    // Check if subsequent number is what it should be
    if (subsequentNumber !== subsequentNumberCheck) {
      // If not, return missing letter with appropriate case
      // by converting what it should be (missing number) into ASCII character
      return String.fromCharCode(subsequentNumberCheck);
    }
  }
}


// First solution
function findMissingLetter(array)
{
  // create new list with all array letters converted into ASCII code with charCodeAt(0)
  const numbersList = array.map((letter) => letter.charCodeAt(letter));
  
  // loop through list of numbers
  for (i = 0; i < numbersList.length; i++) {
      
    // if next number is not current number + 1,
    if (numbersList[i + 1] !== numbersList[i] + 1) {
      
      // return the missing number (current number + 1)
      // converted back into alphabet with String.fromCharCode(n)
      return String.fromCharCode(numbersList[i] + 1);
    }
  }
}


/*
Description:

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

    the array can't be empty
    only non-negative, single digit integers are allowed

Return nil (or your language's equivalent) for invalid inputs.
Examples

Valid arrays

[4, 3, 2, 5] would return [4, 3, 2, 6]
[1, 2, 3, 9] would return [1, 2, 4, 0]
[9, 9, 9, 9] would return [1, 0, 0, 0, 0]
[0, 1, 3, 7] would return [0, 1, 3, 8]

Invalid arrays

[1, -9] is invalid because -9 is not a non-negative integer

[1, 2, 33] is invalid because 33 is not a single-digit integer

*/

// Solution
function upArray(arr){
  
    //if array has negative digits or double digits, return null
    if (arr.some(num => num < 0 || num > 9)) {
      return null;
    }
    
    // if array is empty, return null
    if (arr.length === 0) {
      return null;
    }
    
    let lastIndex = arr.length - 1;
    let output = arr;
  
    // increment last array item by 1
    output[lastIndex]++;
  
    for (let i = lastIndex; i > -1; i--) {    
      if (output[i] > 9) {
        if (i === 0) {
          // set current item to 0, insert 1 into first index of array
          output[i] = 0;
          output.unshift(1);
        } else {
          // set current item to 0, increment next item by 1
          output[i] = 0;
          output[i - 1]++;
        }
      }
    }
  
    return output;
  
  }


/*
Description:

Complete the method which accepts an array of integers, and returns one of the following:

    "yes, ascending" - if the numbers in the array are sorted in an ascending order
    "yes, descending" - if the numbers in the array are sorted in a descending order
    "no" - otherwise

You can assume the array will always be valid, and there will always be one correct answer.

*/

// Solution
function isSortedAndHow(array) {
    const ascend = [...array].sort((a, b) => a < b ? -1 : 1);
    const descend = [...ascend].reverse();
    
    const compareArrays = (arr1, arr2) => arr1.length === arr2.length && arr1.every((e, i) => e === arr2[i]);
    
    if (compareArrays(array, ascend)) {
      return "yes, ascending";
    } else if (compareArrays(array, descend)) {
      return "yes, descending";
    } else {
      return "no";
    };
  }

/*
Description:

Write a function that takes an array of unique integers and returns the minimum number of integers needed to make the values of the array consecutive from the lowest number to the highest number.
Example

[4, 8, 6] --> 2
Because 5 and 7 need to be added to have [4, 5, 6, 7, 8]

[-1, -5] --> 3
Because -2, -3, -4 need to be added to have [-5, -4, -3, -2, -1]

[1] --> 0
[]  --> 0


*/

// Revised solution
function consecutive(arr) {
    const l = arr.length;
    return l ? Math.max(...arr) - Math.min(...arr) - l + 1 : 0;
  
  }


// First solution
function consecutive(arr) {
    // sort array by descending order
    // this way for loop can start at 0
    arr = arr.sort(function(a, b) {return a - b;}).reverse();
      
    // if array length is less than or equal to 1, return 0;
    if (arr.length <= 1) return 0;
      
    // to derive integers needed to make contents of arr consecutive: 
    // sum the difference between each pair of integers
    // then subtract arr.length and add 1
    let sum = 0;
      
    for (let i = 0; i < (arr.length - 1); i++) {
      sum += (arr[i] - arr[i + 1])
    }  
    
    return sum - arr.length + 1;  
      
    }


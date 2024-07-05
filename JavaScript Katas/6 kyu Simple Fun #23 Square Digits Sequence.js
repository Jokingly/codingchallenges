/*
Description:

Task

Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.

Given the first element a0, find the length of the sequence.
Example

For a0 = 16, the output should be 9

Here's how elements of the sequence are constructed:

a0 = 16

a1 = 12 + 62 = 37

a2 = 32 + 72 = 58

a3 = 52 + 82 = 89

a4 = 82 + 92 = 145

a5 = 12 + 42 + 52 = 42

a6 = 42 + 22 = 20

a7 = 22 + 02 = 4

a8 = 42 = 16, which has already occurred before (a0)

Thus, there are 9 elements in the sequence.

For a0 = 103, the output should be 4

The sequence goes as follows: 103 -> 10 -> 1 -> 1, 4 elements altogether.
Input/Output

    [input] integer a0

    First element of a sequence, positive integer.

    Constraints: 1 ≤ a0 ≤ 650.

    [output] an integer


*/


// Revised solution
function squareDigitsSequence(n) {
    let s = new Set();
      
    while (!s.has(n)) {
      s.add(n);
      n = [...''+n].reduce((n, d) => n + d * d, 0);
    }
    
    return s.size + 1;
  }


// First solution
function squareDigitsSequence(a0) {
    // array of calculated sums of squared digits (new sums), starting with a0
    let sumList = [a0];
    
    // add new sums to above array, until a duplicate is found
    while (new Set(sumList).size === sumList.length) {
      // take last sum of above array
      let currentSum = sumList.at(-1);
      // split sum into an array of digits
      // square each digit in array
      // sum items of array
      let newSum = String(currentSum).split("").map(Number).map(x => x**2).reduce((total, currentValue) => total + currentValue);
  
      // insert new sum into array of sums
      // this counts sequences and stores the new sum number to check for duplicates
      sumList.push(newSum);
    }
    
    // return number of sequences
    return sumList.length;
  }


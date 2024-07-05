/*
Description:

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)


*/

// Revised solution
function isIsogram(str){
    return new Set(str.toLowerCase()).size === str.length;
  }


// First solution
function isIsogram(str){
    const setLen = new Set(str.toLowerCase()).size;
    const strLen = str.length;
    
    if (setLen === strLen) {
      return true;
    } else {
      return false;
    };
  }


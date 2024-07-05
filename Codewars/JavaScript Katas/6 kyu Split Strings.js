/*
Description:

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']


*/

// Solution
function solution(str){
  
    if (str.length % 2 != 0) str += "_";
    
    let listItem = "";
    let outputArray = [];
    
    for (i = 0; i < str.length; i+=2) {    
      listItem += str[i];
      listItem += str[i+1];
      outputArray.push(listItem);
      listItem = "";
    }
    
    return outputArray;
      
  }

/*
Description:

Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'


*/

// Revised solution
function solution(str){
    return [...str].reverse().join('');
  }


// First solution
function solution(str){
    return str.split('').reverse().join('');
  }


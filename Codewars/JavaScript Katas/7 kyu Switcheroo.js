/*
Description:

Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'

*/

// Solution
function switcheroo(x){
    switchDict = {
      a: 'b',
      b: 'a'
    }
    
    let output = "";
    
    for (i = 0; i < x.length; i++) {
      if (x[i] === 'a') output += 'b'
      else if (x[i] === 'b') output += 'a'
      else output += x[i]
    }
    
    return output;  
  }

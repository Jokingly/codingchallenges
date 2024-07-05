/*
Description:

Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expandedForm(12); // Should return '10 + 2'
expandedForm(42); // Should return '40 + 2'
expandedForm(70304); // Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!

*/

// Revised solution
function expandedForm(num) {
    return num.toString()
              .split("")
              .reverse()
              .map((n, i) => n * Math.pow(10, i))
              .filter(n => n > 0)
              .reverse()
              .join(" + ");
  }


// First solution
function expandedForm(num) {
    // Parse number into list for iteration
    const numbersList = [...`${num}`].map((num) => +num);
    const output = [];
    
    
    for (i = 0; i < numbersList.length; i++) {
      // If current number is zero, continue to next loop iteration
      if (numbersList[i] === 0) {
        continue;
      }
      
      // Exponent to raise 10 by
      const exponent = numbersList.length - (i + 1);
      // If product is 0, store 1 in variable
      const product = 10**exponent === 0 ? 1 : 10**exponent;
  
      // Expanded digit = current number * product
      const digit = numbersList[i] * product;
          
      // Concatenate digit to output string with respective format
      output.push(digit);
    }  
    
    // Return output string
    return output.join(" + ");
    
  }


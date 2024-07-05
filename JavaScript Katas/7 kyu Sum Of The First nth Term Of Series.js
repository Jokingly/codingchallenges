/*
Description:

Task

Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).
Series:1+14+17+110+113+116+…\mathrm{Series:}\quad 1 + \frac14 + \frac17 + \frac1{10} + \frac1{13} + \frac1{16} + \dotsSeries:1+41​+71​+101​+131​+161​+…

You will need to figure out the rule of the series to complete this.
Rules

    You need to round the answer to 2 decimal places and return it as String.

    If the given value is 0 then it should return "0.00".

    You will only be given Natural Numbers as arguments.

Examples (Input --> Output)

n
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"

Fundamentals
*/

// Revised solution
function SeriesSum(n) {
    let s = 0;
    for (let i = 0; i < n; i++){
      s += 1 / (1 + i * 3);
    }
    return s.toFixed(2);
  }

// First solution
function SeriesSum(n)
{
  let output = 1.00;
  let denominator = 4;
  
  if (n === 0) {
    return "0.00";
  } 
    
  // i starts at 1, 
  // as inputs of 0 and 1 are automatically handled
  for (let i = 1; i < n; i++) {
    output += 1/denominator;
    denominator+=3;  
  }
  return output.toFixed(2);

}


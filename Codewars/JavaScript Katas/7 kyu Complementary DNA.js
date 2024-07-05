/*
Description:

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"


*/

// Solution
function DNAStrand(dna){
    //your code here
    
    // create object of DNA complements as key value pairs
    const complements = {
      A: 'T',
      C: 'G',
      G: 'C',
      T: 'A'
    };
    
    // create result variable
    let result = "";
    
    // iterate through each character of string with for loop
    for (i = 0; i < dna.length; i++) {
      // use current character to access its complement through the complement object
      // add complement to result variable
      const curChar = dna[i];
      const complement = complements[curChar];
      result += complement;
      
    }
    
    // return result variable
    return result;
    
  }


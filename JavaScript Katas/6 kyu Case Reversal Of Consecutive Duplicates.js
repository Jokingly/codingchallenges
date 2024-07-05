/*
Description:
The aim of this Kata is to write a function which will reverse the case of all consecutive duplicate letters in a string. That is, any letters that occur one after the other and are identical.

If the duplicate letters are lowercase then they must be set to uppercase, and if they are uppercase then they need to be changed to lowercase.

Examples:

reverseCase("puzzles")    Expected Result: "puZZles"
reverseCase("massive")    Expected Result: "maSSive"
reverseCase("LITTLE")     Expected Result: "LIttLE"
reverseCase("shhh")       Expected Result: "sHHH"

Arguments passed will include only alphabetical letters A–Z or a–z.


*/

// Solution
function reverseCase(string) {
    string = Array(...string);  
    let consDupes = new Set();
    
    for (i = 0; i < string.length -1 ; i++) {
      if (string[i] === string[i + 1]) {
        consDupes.add(i);
        consDupes.add(i+1);
      };
    };
    
    consDupes.forEach(i => string[i].toUpperCase() === string[i] ? string[i] = string[i].toLowerCase() : string[i] = string[i].toUpperCase());
    
    return string.join('');
    
  }


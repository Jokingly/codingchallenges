/*
Description:
Mount the Bowling Pins!
Task:

Did you ever play Bowling? Short: You have to throw a bowl into 10 Pins arranged like this:

I I I I  # each Pin has a Number:    7 8 9 10
 I I I                                4 5 6
  I I                                  2 3
   I                                    1

You will get an array of integers between 1 and 10, e.g. [3, 5, 9], and have to remove them from the field like this:

I I   I
 I   I
  I   
   I   

Return a string with the current field.
Note that:

    The pins rows are separated by a newline (\n)
    Each Line must be 7 chars long
    Fill the missing pins with a space character ( )

Have fun!


*/

// Revised solution
function bowlingPins(arr) {
    let pin = num => arr.includes(num) ? ' ' : 'I';
    return `${pin(7)} ${pin(8)} ${pin(9)} ${pin(10)}\n ${pin(4)} ${pin(5)} ${pin(6)} \n  ${pin(2)} ${pin(3)}  \n   ${pin(1)}   `;
  }

// First solution
function bowlingPins(arr) {
    
    let field = [
      7, ' ', 8, ' ', 9, ' ', 10, '\n',
      ' ', 4, ' ', 5, ' ', 6, ' ', '\n',
      ' ', ' ', 2, ' ', 3, ' ', ' ', '\n', 
      ' ', ' ', ' ', 1, ' ', ' ', ' '
    ];
              
    for (let i of field) {
      if (typeof i === 'number') {
        if (arr.includes(i)) {
          let indexOfItem = field.indexOf(i);
          field[indexOfItem] = ' ';
        } else {
          let indexOfItem = field.indexOf(i);
          field[indexOfItem] = 'I';
        }
      }
    }
      
    return field.join('');
  }

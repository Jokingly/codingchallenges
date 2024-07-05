/*
Description:

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false


*/


// Revised solution
function validatePIN (pin) {
    return /^(\d{4}|\d{6})$/.test(pin);
  }


// First solution
function validatePIN (pin) {
    //return true or false
    
    if (pin.length === 4) {
      return /\d{4,4}/.test(pin);
    }
    
    if (pin.length === 6) {
      return /\d{6,6}/.test(pin);
    }
    
    return false;
    
  }


/*
Description:

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

eight(dividedBy(three()));

*/

// Solution
function zero(operator) { return operator ? eval("Math.floor(0" + operator) : "0"; }
function one(operator) { return operator ? eval("Math.floor(1" + operator) : "1"; }
function two(operator) { return operator ? eval("Math.floor(2" + operator) : "2"; }
function three(operator) { return operator ? eval("Math.floor(3" + operator) : "3"; }
function four(operator) { return operator ? eval("Math.floor(4" + operator) : "4"; }
function five(operator) { return operator ? eval("Math.floor(5" + operator) : "5"; }
function six(operator) { return operator ? eval("Math.floor(6" + operator) : "6"; }
function seven(operator) { return operator ? eval("Math.floor(7" + operator) : "7"; }
function eight(operator) { return operator ? eval("Math.floor(8" + operator) : "8"; }
function nine(operator) { return operator ? eval("Math.floor(9" + operator) : "9"; }

function plus(num) { return "+" + num + ")"; }
function minus(num) { return "-" + num + ")"; }
function times(num) { return "*" + num + ")"; }
function dividedBy(num) { return "/" + num + ")"; }


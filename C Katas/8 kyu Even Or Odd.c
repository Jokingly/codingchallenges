/*
Description:

Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
*/

// Solution
const char* even_or_odd(int number)
{
  
  int result = number % 2;
  
  if (result == 0)
    {
    return "Even";
  }
  else
    {
    return "Odd";
  }
}

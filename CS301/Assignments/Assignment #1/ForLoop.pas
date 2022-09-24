// Assignment#1-- Pascal
// Thomas Crow
//
// Using JavaScript (not Java, JavaScript is a different language), 
// Rust, and Pascal write a simple FOR loop that adds the first 100 
// positive integers (from 1 to 100, included). 
// Print the result of that summation. 
// Use proper comments in your programs. 


program ForLoop;

  var
    sum,i: integer;

begin
  //Initialize variables
  sum := 0;
  i := 0;
  
  //Add first 100 positive integers, assgn to value sum
  for i := 1 to 100 do
    sum := sum + i;
  
  //Print the value of sum
  writeln('The sum is ',sum);
  
end.
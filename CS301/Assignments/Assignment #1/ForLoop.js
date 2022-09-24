// Assignment #1 -- Javascript
// Thomas Crow
//
// Using JavaScript (not Java, JavaScript is a different language), 
// Rust, and Pascal write a simple FOR loop that adds the first 100 
// positive integers (from 1 to 100, included). 
// Print the result of that summation. 
// Use proper comments in your programs. 

//initialize values
let sum = 0;  

//Add first 100 positive integers, assgn to value sum
for (let i = 0; i < 100; i++, sum += i); //Add positive integers 1 to 100 and assign to i

//Print the value of sum
console.log("The sum is " + sum); 
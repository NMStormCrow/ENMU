// Assignment #1 -- Rust
// Thomas Crow
//
// Using JavaScript (not Java, JavaScript is a different language), 
// Rust, and Pascal write a simple FOR loop that adds the first 100 
// positive integers (from 1 to 100, included). 
// Print the result of that summation. 
// Use proper comments in your programs. 

fn main() {

    //initialize values
    let mut sum = 0;

    //Add first 100 positive integers, assgn to value sum
    for i in 1..101{
        sum += i;
    }

    //Print the value of sum
    println!("The sum is {sum}");

}
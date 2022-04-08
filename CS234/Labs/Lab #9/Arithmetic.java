/*
* Thomas Crow
* Lab #9 
* CS234
*/

public class Arithmetic implements Sequences {
    
//  Declaration of instance variables
    private float initialValue;
    private float element;
    private float difference;

//  Default constructor
    public Arithmetic(float initialValue, float difference) {
   
        setStart(initialValue);
        this.difference = difference;
        
    }

//  Method: getInitialValue
//  Purpose: Get the starting value of the arithmetic sequence
//  Arguments: None
//  Returns:  The starting value of the arithmetic sequence as a float

    public float getInitialValue() {

        return initialValue;

    }
 
//  Method: getNext
//  Purpose: Get the next element of the arithmetic sequence
//  Arguments: None 
//  Returns: The next element of the arithmetic sequence as a float 

    public float getNext() {
        this.element += difference;
        return this.element;
    }

//  Method: restart
//  Purpose: Resets the sequence to the initial value of the arithmetic sequence
//  Arguments: None
//  Returns: None

    public void restart() {
        this.element = this.initialValue;
    } 

//  Method: setStart
//  Purpose: Set the initial value of the arithmetic sequence
//  Arguments: The initial value of the arithmetic sequence as a float
//  Returns: None

    public void setStart(float value) {

        this.initialValue = value;
        this.element = this.initialValue;

    }

//  Method: getNthElement
//  Purpose: Return the value of the Nth element of an arithmetic sequence
//  Arguments: The Nth value as an int
//  Returns: The value of the Nth element of an arithmetic sequence as a float

    public float getNthElement(int element) {

        return (this.initialValue + (this.difference * (element - 1)));

    }

}

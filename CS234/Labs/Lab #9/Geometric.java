/*
* Thomas Crow
* Lab #9 
* CS234
*/

import java.lang.Math;

public class Geometric implements Sequences {

    //  Declaration of instance variables
    private float initialValue;
    private float element;
    private float ratio;

//  Default constructor
    public Geometric(float initialValue, float ratio) {
        
        setStart(initialValue);
        this.ratio = ratio;

    }

//  Method: getInitialValue
//  Purpose: Get the starting value of the geometric sequence
//  Arguments: None
//  Returns:  The starting value of the geometric sequence as a float

    public float getInitialValue() {

        return initialValue;

    }

//  Method: getNext
//  Purpose: Get the next element of the geometric sequence
//  Arguments: None 
//  Returns: The next element of the geometric sequence as a float 

    public float getNext() {

        this.element = this.element * ratio;
        return this.element;

    }

//  Method: restart
//  Purpose: Resets the sequence to the initial value of the geometric sequence
//  Arguments: None
//  Returns: None

    public void restart() {
        
        this.element = this.initialValue;

    } 

//  Method: setStart
//  Purpose: Set the initial value of the geometric sequence
//  Arguments: The initial value of the geometric sequence as a float
//  Returns: None

    public void setStart(float value) {

        this.initialValue = value;
        this.element = this.initialValue;

    }

//  Method: getNthElement
//  Purpose: Return the value of the Nth element of an geometric sequence
//  Arguments: The Nth value as an int
//  Returns: The value of the Nth element of an geometric sequence as a float

    public float getNthElement(int element) {

        return (float) (this.initialValue * (Math.pow(this.ratio, (element  - 1))));

    }


}

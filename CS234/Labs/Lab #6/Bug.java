/*
* CS234
* Thomas Crow
* Lab #6 Question #1
*
* Requirements: Write a class definition named Bug (i.e., .java file without the main method) 
                that models a bug moving along a horizontal line. The bug moves either to the 
                right or left. Initially, the bug moves to the right starting at position 10, 
                but it can turn to change its direction. In each move, its position changes by 
                one unit in the current direction. 
                
                Therefore, you need to have one instance variable to keep track of the current 
                position and one instance variable to keep track of the current direction (right 
                or left). No extra instance variables are allowed.  
                
                Provide the following methods: 1) a method to move the bug, 2) a method to turn 
                direction, and 3) a method to get the position of the bug. These methods are 
                the only allowed to modify the instance variables (i.e., no direct access to 
                these instance variables). 
                No extra methods are allowed. 
                
*/

public class Bug {

//  Declaration of instance variables
    private static String BugDirection;
    private static int BugPostition;

//  Default contstructor
    public Bug() {
        BugDirection = "Right";
        BugPostition = 10;
    }

//  Method: move
//  Purpose: Move the bug one postition in the direction it's facing
//  Arguments: None
//  Returns: None

    public void move() {
        if (BugDirection == "Right")
            BugPostition += 1;
        else
            BugPostition -= 1;
    }

//  Method: turn
//  Purpose: Change direction of bug
//  Arguments: None
//  Returns: None

    public void turn() {
        
        if (BugDirection == "Right")
            BugDirection = "Left";
        else
            BugDirection = "Right";
    }

//  Method: getPostition
//  Purpose: Provides the current posttition of the bug
//  Arguments: None
//  Returns: Int value of bug's postition 

    public int getPostition() {
        return BugPostition;
    }
}
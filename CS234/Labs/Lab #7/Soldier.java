/*
* CS234
* Thomas Crow
* Lab #7 Part B
*
* Requirements: Write a class definition named Soldier (i.e., a .java file without the main 
                method). 
                
                A given soldier has a value for health, the type of soldier, and a list of 
                weapons. This information needs to be stored as instance variables. No extra 
                instance variables are allowed. 
                
                There must be two constructors. A default constructor and custom constructor.  
                The default constructor initializes the health with a value of 10, the soldier 
                type with an empty string, and an empty list of weapons. 
                The custom constructor receives the health and type, and initializes an empty 
                list of weapons. 
                
                There must be methods to get and set the soldier’s health value and the soldier’s 
                type. 
                Similarly, there must be a method to add a weapon to the list of weapons for 
                each soldier, and a method to get that list of weapons. 
                
                A soldier can shoot enemies. Therefore, you need to create a method for shooting 
                an enemy (which is also a soldier). Every time a soldier shoots an enemy, the 
                health of that enemy is reduced by 1 unit. 
                
                Finally, a getInfo() method is expected to get all the soldier’s information.  
                
                No extra methods are needed nor allowed.     
*/

import java.util.ArrayList;

public class Soldier {

    //  Declaration of instance variables
    private int health;
    private String soldierType;
    private ArrayList<String> weaponList = new ArrayList<String>();

    //  Default contstructor
    public Soldier() {
        health = 10;
        soldierType = "";
    }

//  Method: 
//  Purpose: 
//  Arguments: 
//  Returns: 

}

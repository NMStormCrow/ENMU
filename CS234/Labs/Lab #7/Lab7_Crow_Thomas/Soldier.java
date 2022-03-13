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
    private int soldierHealth;
    private String soldierType;
    private ArrayList<String> weaponList = new ArrayList<String>();

    //  Default contstructor
    public Soldier() {
        soldierHealth = 10;
        soldierType = "";
    }

    // Alternate constructor
    public Soldier(int Health, String type)  {
        soldierHealth = Health;
        soldierType = type;
    }

//  Method: setSoldierType 
//  Purpose: Sets the type of the solider
//  Arguments: The type of soldier as an string
//  Returns: None
    public void setSoldierType(String type) {
        soldierType = type;
    }

//  Method: setHealth 
//  Purpose: Sets the health of the solider
//  Arguments: Heath value as an int
//  Returns: None
    public void setHealth(int health) {
        soldierHealth = health;
    }

//  Method: getHealth 
//  Purpose: Gets the health of the solider
//  Arguments: None
//  Returns: The health of the soldier as an int value
    public int getHealth() {
        return soldierHealth;
    }

//  Method: addWeapon 
//  Purpose: Adds a weapon to the soliders list
//  Arguments: A new weapon as a string value
//  Returns: None
    public void addWeapon(String weapon) {
        weaponList.add(weapon);
    }

//  Method: shootEnemy 
//  Purpose: Shoots an enemy, reducing thier health by one
//  Arguments: The enemy, as type soldier
//  Returns: None
    public void shootEnemy(Soldier enemy) {
        int enemyHealth = enemy.getHealth();
        System.out.printf("The %s is shooting at the %s\n", soldierType, enemy.soldierType);
        enemy.setHealth(enemyHealth - 1);
        if (enemy.getHealth() <= 0)
            System.out.printf("The %s is dead\n", enemy.soldierType); 
    }

//  Method: getInfo 
//  Purpose: Returns information about the solider
//  Arguments: None
//  Returns: Solider info as a string
    public String getInfo() {
        String info = new String("The " + soldierType + " has health of " + soldierHealth + " and has the following weapons: " + weaponList);
        return info;
    }
}
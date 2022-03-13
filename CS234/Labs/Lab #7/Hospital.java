/*
* CS234
* Thomas Crow
* Lab #7 Part A
*
* Requirements: Write  a  class  definition  named  Hospital  (i.e.,  .java  file  without  the  main 
                method).  
                
                You need to have one instance variable to store a hospital’s name. No extra 
                instance variables are allowed.  
                
                A given hospital does one action and is to heal patients. Therefore, you need 
                to create a non-static method that receives as parameter a patient. The method 
                needs to check the patient’s health. If the health is 0 units or less, sadly, 
                the patient is dead. Otherwise, the hospital increases the patient health by 1 
                unit. The method does not return anything. 
                
                The name for each hospital is assigned in the constructor for that instance. 
                
                No extra methods are needed nor allowed.  
*/

public class Hospital  {

//  Declaration of instance variables
    private String HospitalName;

//  Default contstructor
    public Hospital(String Name) {
        HospitalName = Name;
    }

//  Method: healPatient
//  Purpose: Heals Patient by 1 as long as the health is greater than 0
//  Arguments: Patient as a string
//  Returns: None
    public void healPatient(Soldier patient) {
        int health = patient.getHealth();
        if (health > 0) {
            patient.setHealth(health + 1);
        }
        else {
            System.out.printf("The patient already is dead\n");
        }
    }
}
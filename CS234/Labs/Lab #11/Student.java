/*
* Thomas Crow
* Lab #11
* CS234
*/

import java.util.ArrayList;

public class Student {

//  Declare instance variables
    private String sid;
    private String name;
    private String major;
    private ArrayList<Double> grades = new ArrayList<Double>();

//  Default constructor
    public Student(String sid, String name, String major) {
        this.sid = sid;
        this.name = name;
        this.major = major;
    }

//  Method: getSid()
//  Purpose: Obtain the student ID from the student
//  Arguments: None
//  Returns: The Student ID as a string value

    public String getSid() {
        return this.sid;
    }

//  Method: getName()
//  Purpose: Obtain the name of the student
//  Arguments: None
//  Returns: The name of the student as a string value

    public String getName() {
        return this.name;
    }

//  Method: getMajor()
//  Purpose: Obtain the major of the student
//  Arguments: None
//  Returns: The major of the student as a string value

    public String getMajor() {
        return this.major;
    }

//  Method: getGrades()
//  Purpose: Obtain the grades of the student
//  Arguments: None
//  Returns: The student's grades as an arraylist of doubles

    public ArrayList<Double> getGrades() {
        return this.grades;
    }

//  Method: storeGrade()
//  Purpose: Add a grade to the student's record
//  Arguments: The grade as a double
//  Returns: None

    public void storeGrade(Double grade) {
        this.grades.add(grade);
    }
}

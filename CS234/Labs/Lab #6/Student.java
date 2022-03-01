/*
* CS234
* Thomas Crow
* Lab #6 Question #2
*
* Requirements: Implement a class definition named Student (i.e., 
                a .java file without the main method). For this exercise, a student has a name 
                and a list of scores. 
                You need to model this information using one instance variable for the name, 
                and one instance variable for the list of scores. No extra instance variables 
                are allowed.  
                
                You need to define methods to set 1) the name, 2) get the name, 3) add a score, 
                4) get the total of scores (the addition of all scores), 5) get the average 
                score, and 5) get the higher score. These methods are the only allowed to modify 
                the instance variables (i.e., no direct access to these instance variables). 
                No extra methods are allowed.               
*/

import java.util.ArrayList;

public class Student {

//  Declaration of instance variables
    private String StudentName;
    private ArrayList<Double> StudentGrades = new ArrayList<Double>();

//  Default contstructor
    public Student() {
    }

//  Method: setName
//  Purpose: Set the name of student
//  Arguments: None
//  Returns: None

    public void setName(String name) {
        StudentName = name;
    }

//  Method: getName
//  Purpose: Return value of student's name 
//  Arguments: None
//  Returns: String value of student's name

    public String getName() {
        return StudentName;
    }

//  Method: addScore
//  Purpose: Add a score to the student's list of scores
//  Arguments: Student's score as double
//  Returns: None

    public void addScore(double score) {
        StudentGrades.add(score);
    }

//  Method: getTotalScore
//  Purpose: Return the total score of the student
//  Arguments: None
//  Returns: Student's total score value as a double 

    public double getTotalScore() {
        double totalScore = 0;
        for (double d : StudentGrades)
            totalScore += d;
        return totalScore;
    }

//  Method: getTotalScore
//  Purpose: Return the average score of the student
//  Arguments: None
//  Returns: Student's average score value as a double 

    public double getAverageScore() {
        double totalScore = getTotalScore();
        double averageScore = totalScore / StudentGrades.size();
        return averageScore;
    }

//  Method: getHighScore
//  Purpose: Return the highest score of the student
//  Arguments: None
//  Returns: Student's highest score value as a double 

    public double getHighScore() {
        double highScore = 0;
        for (double d : StudentGrades)
            if (d > highScore)
                highScore = d;
        return highScore;
    }
}
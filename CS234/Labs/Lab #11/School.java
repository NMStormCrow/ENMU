/*
* Thomas Crow
* Lab #11
* CS234
*/

import java.util.HashMap;
import java.util.Random;

public class School {


//  Declare instance variables
    private HashMap<String, Student> students = new HashMap<>();
    private Random rand = new Random();

//  Default constructor
    public School() {

    }

//  Method: addStudent()
//  Purpose: Adds a student to the school.
//  Arguments:  The student ID as a string
//              The student's name as a string
//              The student's major as a string   
//  Returns:    None

    public void addStudent(String sid, String name, String major) {

        Student student = new Student(sid, name, major); 
        students.put(sid,student);
        generateGrades(student, 0, 100);

    }

//  Method:    generateGrades()
//  Purpose:   Generates five random grades for a given student
//  Arguments: (The student as a class instance of student,
//             the minimum and maxium value of the random grade values as doubles)
//  Returns:   None

    public void generateGrades(Student s, double min, double max) {

        double grade = 0;
        
        for (int i = 0; i < 5; i++) {
            grade =  this.rand.nextDouble(min, max);
            s.storeGrade(grade);
        }

    }

//  Method: getStudentInfo()
//  Purpose: Displays the information for a student. It displays the students ID, name,
//           major, a list of their grades, and the average of their grades.
//           The grade average will be to two decimal points
//           If the student ID does not exist, an error message will be displayed to the user.
//  Arguments: The student ID as a string
//  Returns: None

    public void getStudentInfo(String sid) {

        if (this.students.containsKey(sid)) {
            System.out.println("Test");
        }
        else {
            System.out.println("There is no student with associated SID: " + sid);
        }
    }
}

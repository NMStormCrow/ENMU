public class schoolTester {
    
    public static void main(String[] args) {

        //Creates a new object for the school
        School mySchool = new School();

        // Creates three students
        mySchool.addStudent("001", "Emma", "Art");
        mySchool.addStudent("002", "John", "CS");
        mySchool.addStudent("003", "Carlos", "Math");

        // Gets the information for one student
        mySchool.getStudentInfo("003");
        // Gets the information for another student
        mySchool.getStudentInfo("005");
    }
}

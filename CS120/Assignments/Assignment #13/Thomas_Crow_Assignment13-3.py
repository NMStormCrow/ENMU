#   Assignment #12 Question #1
#
#   Thomas Crow
#   Date 11/20/2021
#
#   Requirements: Modify the student from the chapter by adding a mutator method
#                 that records a grade for a student. Here is the specification of the new
#                 method:
#                 addGrade(self, gradePoint, credits) gradePoint is a float that represents
#                 a grade (e.g., A = 4.0, A-=3.7, B+ = 3.3, etc), and credits is a float
#                 indicating the number of credit hours for the class. Modify the student
#                 object by adding this grade information.
#
#                 Use the updated class to implement a simple program for calculating
#                 GPA. Your program should create a new student object that has 0 credits
#                 and 0 gaulity points (the name is irrelevant). Your program should then
#                 prompt the user to enter course information (gradePoint and credits) for
#                 a serues if courses, and then print out the final GPA achieved.
##################################################

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    
    def addGrade(self, gradePoint, credits):
        self.hours = self.hours + credits
        self.qpoints = self.qpoints + (gradePoint * credits)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

def makeStudent ():
    name = input ("Please enter the name of the student: ")
    hours = 0
    qpoints = 0
    return Student(name, hours, qpoints)
        
def main():
    student = makeStudent()
    userChoice = True

    while (userChoice == True):
        gradePoint = float(input("Please enter the gradepoint for a class: "))
        creditHours = float(input("Please enter the credit hours for the class: "))
        student.addGrade(gradePoint, creditHours)
        loopBool = True
        while (loopBool == True):
            userInput = input("Do you have more classes to enter?  Type yes to continue. Type no to quit: ")
            if (userInput.lower() == "yes"):
                userChoice = True
                loopBool = False
            elif (userInput.lower() == "no"):
                userChoice = False
                loopBool = False
            else:
                print("You did not enter a valid entry. Please try again.")
                loopBool = True
    print(f"The grade point average for {student.getName()} is: {round(student.gpa(),2)}")
    



if __name__ == '__main__':
    main()

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

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

def makeStudent (infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)
        
def main():
    # open the input file for reading
    filename = input ("Enter the name of the grade file: ")
    infile = open(filename, 'r')
    
    # set best to the record for the first student in the file
    best = makeStudent(infile.readline())
    
    # process subsequent lines of the file
    for line in infile:
        # turn the line into a student record
        s = makeStudent(line)
        # if this student is best so far , remember it .
        if s.gpa() > best.gpa():
            best = s
    infile.close()
    # print information about the best student
    print ("The best student is: ", best.getName())
    print ("hours: ", best.getHours())
    print ("GPA: ", best.gpa())

if __name__ == 'main':
    main()

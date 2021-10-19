#   Assignment #9 Question #2
#
#   Thomas Crow
#   Date 10/17/2021
#
#   Requirements:
#
#   A student will not be allowed to sit in exam if his/her attendance is less than 80%.
#   Take following input from user Number of classes held Number of classes attended.
#
#   Print percentage of class attended, and print the result of student is allowed to sit in exam or not.
#

##################################################################################################################
#  Description: Prompts user for classes attended and offered. Prints whether studen can attend class based on
#               80% attendance requirement.
#  Input: None
#  Output: None

def qualifyStudent():

    print("Students will not be allowed to sit in the exam if their attendance is less than 80%")
    classesGiven = eval(input("How many classes have been held? "))
    classesAttended = eval(input("How many classes have you attended? "))
    pecentageAttended = classesAttended / classesGiven
    print(f"The percentage of classes attended is: {format(pecentageAttended * 100,'.2f')}%")

    if (pecentageAttended < 0.8):
        print("Because your attendance is below 80% you are not allowed to sit in the exam.")
    else:
        print("Based on your attendance, you are allowed to sit in the exam.")

##################################################################################################################

def main():

    qualifyStudent()


main()

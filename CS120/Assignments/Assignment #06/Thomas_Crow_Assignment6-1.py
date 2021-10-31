# Assignment #6 Question #1
#
# Thomas Crow
# Date 9/26/2021
#
#
#    A certain CS professor gives 100-point exams that are graded on the scale 90- 100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.
#
#    Write a program that accepts an exam score as input and prints out the corresponding grade.
#
#    Remark: Please do not use if elseif statement. If you use this statement, I will cut some points.
#
#    Hint: int(63/10)=6
#
#    Note: This program is not equipped to handle entries outside the 0-100 grade range

def main():

#   Initialize LetterGrade string
    LetterGrade = 'FFFFFFDCBAA'

    ExamScore = eval(input("Please enter the exam score: "))
    ExamGrade = LetterGrade[int(ExamScore/10)]
    print("The letter grade for the exam is:",ExamGrade)


main()

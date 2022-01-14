#  CS 120 Final Question #6
#  Thomas Crow

# Please write a Python program that help a 4th grader practicing basic addition and subtraction. Every time, the program will randomly generate 10 questions of 1 digit addition, 
# subtraction, multiplication and division. At the end of 2 questions, ask the user whether more practice or no. If yes, another round of 2 random questions.
# Note: For division, the result can only be an integer. You will get extra points if you used the graphical user interfaces (UGI) to design this program. 

import random
    
def createProblem():

    operatorList = []
    operatorList.append("+")
    operatorList.append("-")
    operatorList.append("*")
    operatorList.append("/")

    for i in range(10):
        firstNumber = random.randint(0,9)
        secondNumber = random.randint(0,9)
#        operator = random.choices(operatorList)
        print(f"{firstNumber}")
        print(str(random.choices(operatorList)))
        print(f"{secondNumber}")
        print(f"=")
        print()
        if ((i+1) % 2 == 0):
            likeToContinue = input("Type yes to continue.")
            if (likeToContinue != "yes"):
                return
    
    return





def main():
    createProblem()


main()
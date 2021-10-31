# Assignment #8 Question #4
#
# Thomas Crow
# Date 10/10/2021
#
#   Requirements:
#
#
#   Use the functions to implement a program that computes the sum of the squares of numbers read from a file.
#   Your program should prompt for a file name and print out the sum of the squares of the values in the file.



##################################################################################################################
#  Obtains values from file specified from users
#  Input: None
#  Output: List of numbers from specified file

def ObtainValues():

    list_of_numbers = []


    FileName=input("Please enter the filename: ")
    InFile=open(FileName, 'r')

    for EachLine in InFile.readlines():
        list_of_numbers.append(int(EachLine))

        #   Close open files
    InFile.close

    return list_of_numbers

##################################################################################################################

##################################################################################################################
#  Calculate the sum of the squares of numbers from a list
#  Input: List of numbers
#  Output: Sum

def CalculateSquaredSums(numberList):

    sum = 0

    for i in range(len(numberList)):
        sum = sum + (numberList[i] ** 2)

    return sum

##################################################################################################################

##################################################################################################################
#  Prints the sum of the squares of numbers
#  Input: The sum of the squares of numbers
#  Output: None

def print_sum_of_squared_numbers(sum):

    print(f"The sum of the squares of numbers is {sum}.")



##################################################################################################################

def main():

    numlist = ObtainValues()
    sumoflistsquare = CalculateSquaredSums(numlist)
    print_sum_of_squared_numbers(sumoflistsquare)
    
main()

# Assignment #6 Question #3
#
# Thomas Crow
# Date 9/26/2021
#
#
#    Expand your solution to the practice problem to allow the calculation of a complete name such as ‘John Marvin Zelle" or ‘John Jacob Jingleheimer Smith." The total value is just the sum of the numeric values of all the names.
#
#    Hint: use the function split() to get the separate words
#
#          use s.lower() to get all lowercase letters
#


def main():

    UserName = input("Please enter your full name: ")
    UserNameSplit = UserName.split()

#   Initialize the TotalSum to zero
    TotalSum = 0

#   Determine the number of names entered
    numNameElements = len(UserNameSplit)

#   Run loop for each name value that is contained in UserNameSplit
    for i in range(numNameElements):
         OuterLoopLen = len(UserNameSplit[i])
         OuterLoopName = UserNameSplit[i]
#        Run loop for each letter in the name current selected
         for j in range (OuterLoopLen):
             InnerLoopChar = OuterLoopName[j].lower()
             InnerLoopCharValue = ord(InnerLoopChar) - 96
             TotalSum = TotalSum + InnerLoopCharValue

    print("The numeric value of", UserName,"is:", TotalSum)

main()

#   Assignment #11 Question #5
#
#   Thomas Crow
#   Date 11/07/2021
#
#   Requirements: Write a program to print out the truth table for any Boolean
#                 expression. (contains at most two variables.)
#
#                 Hint: eval(expression)
#                 Def function(expres)
#
#                 Main()
#                 expres=?
#                 function(expres)
#
#

##################################################################################################################
#  Description:  Prints truth table based on user inputed boolean expression 
#  Input: Expression from user as string list
#  Output: None

def printTruthTable(boolExpression):

    variables = []
    duplicate = False

    boolExpression = boolExpression.strip()
    expression = boolExpression.split(' ')
    for i in range(len(expression)):
        if (expression[i] != "and") and (expression[i] != "or") and (expression[i] != "not"):
            for j in range(len(variables)):
                if expression[i] == variables[j]:
                    duplicate = True
            if duplicate == False:
                variables.append(expression[i])
            duplicate = False
    
    if len(variables) > 2:
        print("Please only enter up to two variables.")
        return
    
    if len(variables) == 0:
        print("Please at least one variable.")
        return
    
 
    if len(variables) == 2:
        locals()[variables[0]] = True
        locals()[variables[1]] = True
        print(f"|   {variables[0]} \t\t\t|   {variables[1]} \t\t\t|   {boolExpression} \t\t\t|")
        print(f"|   {eval(variables[0])} \t\t|   {eval(variables[1])} \t\t|   {eval(boolExpression)} \t\t\t|")
        locals()[variables[0]] = True
        locals()[variables[1]] = False
        print(f"|   {eval(variables[0])} \t\t|   {eval(variables[1])} \t\t|   {eval(boolExpression)} \t\t\t|")
        locals()[variables[0]] = False
        locals()[variables[1]] = True
        print(f"|   {eval(variables[0])} \t\t|   {eval(variables[1])} \t\t|   {eval(boolExpression)} \t\t\t|")
        locals()[variables[0]] = False
        locals()[variables[1]] = False
        print(f"|   {eval(variables[0])} \t\t|   {eval(variables[1])} \t\t|   {eval(boolExpression)} \t\t\t|")

    if len(variables) == 1:
        locals()[variables[0]] = True
        print(f"|   {variables[0]} \t\t\t|   {boolExpression} \t\t\t|")
        print(f"|   {eval(variables[0])} \t\t|  {eval(boolExpression)} \t\t\t|")
        locals()[variables[0]] = False
        print(f"|   {eval(variables[0])} \t\t|  {eval(boolExpression)} \t\t\t|")
        

##################################################################################################################

def main():
    booleanExpression = input("Please enter the boolean expression: ")
    printTruthTable(booleanExpression)

main()

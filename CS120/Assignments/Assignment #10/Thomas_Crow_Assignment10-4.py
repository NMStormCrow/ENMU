#   Assignment #10 Question #4
#
#   Thomas Crow
#   Date 10/23/2021
#

#   Requirements: The days of the year are often numbered from 1 through 365 (or 366). This number can be computed in three steps using int arithmetic:
#                 (a) dayNum = 31(month - 1) + day
#                 (b) if the month is after February subtract (4(month) + 23)/ /10
#                 (c) if it's a leap year and after February 29, add 1
#                   
#                 Write a program that accepts a date as month/day/year, verifies that it is a valid date (see class example), and then calculates the corresponding day number.
#
# 

import math


##################################################################################################################
#  Description:  Determines the day of year for a given date
#  Input: None
#  Output: None

def dateCalculator():
    
    userInputtedDate=input("Please enter a date in the format mm/dd/yyyy: ") 
    userMonth, userDay, userYear=userInputtedDate.split("/")
    formattedDay = int(userDay)
    formattedMonth = int(userMonth)
    formattedYear = int(userYear)
    leapYear = isLeapYear(formattedYear)
    userDayNum = calcDayNum(formattedMonth, formattedDay, leapYear)
    monthsWith31Days=[1,3,5,7,8,10,12]
    monthsWith30Days=[4,6,9,11]


    if (int(userMonth) in monthsWith31Days):
        if (int(userDay)>31):
            print("You entered a date with too many days in the month.")
        elif (int(userDay)<1):
            print("You entered a date with too few days in the month.")
        else:
            print(f"The date is: {userInputtedDate}")
            if (leapYear):
                print(f"This is day {userDayNum} of 366.")
            else:
                print(f"This is day {userDayNum} of 365.")
    elif (int(userMonth) in monthsWith30Days):
        if (int(userDay)>30):
            print("You entered a date with too many days in the month.")
        elif (int(userDay)<1):
            print("You entered a date with too few days in the month.")
        else:
            print(f"The date is: {userInputtedDate}")
            if (leapYear):
                print(f"This is day {userDayNum} of 366.")
            else:
                print(f"This is day {userDayNum} of 365.")
    elif (int(userMonth)==2):
        if (leapYear) and (int(userDay)>29):
            print("You entered a date with too many days in the month.")
        elif (leapYear) and (int(userDay)<1):
            print("You entered a date with too few days in the month.")
        elif (leapYear):
            print(f"The date is: {userInputtedDate}")
            print(f"This is day {userDayNum} of 366.")
        elif ~(leapYear) and (int(userDay)>28):
            print("You entered a date with too many days in the month.")
        elif ~(leapYear) and (int(userDay)<1):
            print("You entered a date with too few days in the month.")
        else:
            print(f"The date is: {userInputtedDate}")
            print(f"This is day {userDayNum} of 365.")
    else:
        print("You entered an invalid month.")


##################################################################################################################

##################################################################################################################
#  Description:  Determines is a year is a leap year
#  Input: Year as an int value
#  Output: Boolean value if leap year is true

def isLeapYear(year):

    if ((year % 4) == 0):
        if ((year % 100) == 0):
            if ((year% 400) == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

##################################################################################################################

##################################################################################################################
#  Description:  Determines the day of the year
#  Input: Int values of the month and day, boolean value of leap year
#  Output: Day of year as an int value

def calcDayNum(month, day, leapyear):

    dayNum = 31 * (month - 1) + day

    if (month > 2):
        dayNum = (dayNum - (((4 * month) + 23) / 10)) 
        if (leapyear):
            dayNum = dayNum + 1

    return int(math.ceil(dayNum))
             
##################################################################################################################

def main():

    dateCalculator()

main()

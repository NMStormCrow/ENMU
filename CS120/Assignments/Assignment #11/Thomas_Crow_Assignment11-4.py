#   Assignment #11 Question #4
#
#   Thomas Crow
#   Date 11/07/2021
#
#   Requirements: Write a program that computes the fuel efficiency of a multi-leg 
#                 journey. The program will first prompt for the starting odometer
#                 reading and then get information about a series of legs, such as
#                 the current odometer reading and the amount of gas used, from a
#                 file. The user signals the end of the trip with a blank line.
#
#                 The program should print out the miles per gallon achieved on
#                 each leg and the total MPG for the trip.

##################################################################################################################
#  Description: Obtains the starting odometer reading from the user
#  Input: None
#  Output: Starting odometer reading 

def obtainStartingOdometer():

    startingOdometer = -1

    while startingOdometer < 0:
        startingOdometer = eval(input("Please enter the starting odometer value: "))
        if (startingOdometer < 0):
            print("Please enter a valid odometer value")
    
    return startingOdometer

##################################################################################################################

##################################################################################################################
#  Description: Starting with a user inputted odometer value, this program reads from a file additional 
#               odometer and fuel usage values
#  Input: Start odometer value
#  Output: None

def calculateTripMileage(startOdometer):
    
    legOdd = []
    legFuel = []
    legDistance = []

    currentOdometer = startOdometer
    totalMileage = 0
    totalFuel = 0

    filename = input("Please enter the filename of the milage and fuel information: ")
    infile = open(filename)
    line = infile.readline()
    line = line.strip()
    while (line != ""):
        
        leginfo = line.split(',')
        legOdd.append(float(leginfo[0]))
        legFuel.append(float(leginfo[1])) 
        line = infile.readline()
        line = line.strip()
    infile.close()

    for i in range(len(legOdd)):
        legDistance.append(legOdd[i] - currentOdometer)
        totalMileage = totalMileage + legDistance[i]
        totalFuel = totalFuel + legFuel[i]
        currentOdometer = legOdd[i]
        print(f"Leg {i+1} was {legDistance[i]} miles. {legFuel[i]} gallons was used. The MPG was {round((legDistance[i] / legFuel[i]),2)} miles per gallon. ") 
    
    print(f"The total distance was {round(totalMileage,2)} miles. The total MPG was {round((totalMileage / totalFuel),2)}.")



##################################################################################################################


def main():
    startOdometerReading = obtainStartingOdometer()
    calculateTripMileage(startOdometerReading)



main()

# Assignment #3 Question #2
#
# Thomas Crow
# Date 9/05/2021
#
# Requirements:
#
# Here are some formulas that might be useful:
#
#              height
# length =   -----------
#            sin angle θ
#
#               π
# radians =   ----- degrees
#              180
#
#
#
# Inputs:
# house_height = height of house
# ladder_angle = elevation angle of ladder
#
# Outputs:
# length_ladder = necessary length of the ladded. (The hypotenuse of the right angle triangle formed)
#
# Note for instructor:
# This calulator rounds up the output to the next whole value.
# Because you cannot go to Home Depot and buy a 13.4732 foot ladder! Well, maybe their cheap 14 foot one! :-)
# Or in fractions of metric measurements in countries lucky/smart enough to not use feet as a form of measurement. :-D

import math

def main():

#   Statement of program's purpose
    print("This program determines the length of a ladder, rounded up to the next whole value, required to reach a given height when leaned against a house.")
    print("The height of the house and the angle of the ladder will be used to determine the length required.")
    print()

#   Input from user
    house_height = eval(input("Please enter the height of the house: "))
    ladder_angle = eval(input("Please enter the elevation angle of the ladder leaned on the house: "))

#   The part where we make the computer do all the work
    angle_in_radians = (math.pi / 180) * ladder_angle
#   You could also use the math.radians() function to convert degrees to radians, but where is the fun in that when you gave the formula? :-)
    length_ladder = house_height / (math.sin(angle_in_radians))

#   Output to user
    print()
    print(f"The height of the house was supplied as: {house_height}.")
    print(f"The supplied elevation angle of the ladder was {ladder_angle}°.")
    print(f"The necessary length of the ladder, rounded up to the next whole value, is: {math.ceil(length_ladder)}.")

main()

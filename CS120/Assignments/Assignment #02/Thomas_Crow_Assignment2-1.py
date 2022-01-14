# Assignment #2 Question #1
#
# Thomas Crow
# Date 8/28/2021
#
# Requirements: Write a program that converts distances measured in kilometers to miles. Hint: One kilometer is approximately 0.62 miles.
#
# Formula: miles = (kilometers * 0.62137119)
#
# Note for Instructor:
#
# I have formatted the output to display the floating point value to two decimal places

def main():

    distance_in_kilometers=eval(input("What is the distance in Kilometers? "))
    distance_in_miles=(distance_in_kilometers * 0.62137119)
    print ("The distance is", format(distance_in_miles, '.2f'), "miles.")

main()

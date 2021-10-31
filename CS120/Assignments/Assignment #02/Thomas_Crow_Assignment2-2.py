# Assignment #2 Question #2
#
# Thomas Crow
# Date 8/28/2021
#
# Requirements: Write a program that converts temperatures from Fahrenheit to Celsius
#
# Formula: Celsius = (Fahrenheit - 32) * 5/9
#
# Note for Instructor:
#
# I have formatted the output to display the floating point value to one decimal place


def main():

    temp_in_fahrenheit=eval(input("What is the temperature in Fahrenheit? "))
    temp_in_celsius=(temp_in_fahrenheit - 32) * (5/9)
    print ("The temperature is", format(temp_in_celsius, '.1f'), "degrees Celsius.")

main()

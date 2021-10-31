# Assignment #3 Question #1
#
# Thomas Crow
# Date 9/04/2021
#
# Requirements:
# Write a program to calculate the volume and surface area of a sphere from its radius, given as input.
# Here are some formulas that might be useful:
# V = 4/3πr³
# A = 4πr²
#
# Inputs:
# sphere_radius = the sphere of the sphere
# round_to = the number of decimal places the user wishes to display
#
# Outputs:
# sphere_volume = the volume of the sphere
# sphere_area = the surface area of the sphere


import math

def main():
###################################################################################
#   A little superfluous ASCII art.  Credit of art on my part not intended nor implied.
    print("                 ____")
    print("            ,dP9CGG88@b,")
    print("          ,IP""YICCG888@@b,")
    print("         dIi   IICGG8888@b")
    print("        dCIIiciIICCGG8888@@b")
    print("        GCCIIIICCCGGG8888@@@")
    print("        GGCCCCCCCGGG88888@@@     Sphere Volume and Area Calculator")
    print("        GGGGCCCGGGG88888@@@@...")
    print("        Y8GGGGGG8888888@@@@P.....")
    print("         Y88888888888@@@@@P......")
    print("         `Y8888888@@@@@@@P'......")
    print("            `@@@@@@@@@P'.......")
    print("                ........")
    print()
##################################################################################

#   Statement of program's purpose
    print("This program calculates the volume and surface area of a sphere from the radius provided.")
    print("You will be able to specify the number of decimal places you wish to display.")
    print()

#   Input from user
    sphere_radius = eval(input("Please enter the radius of the sphere: "))
    round_to = eval(input("Please enter the number of decimal places you would like to display: "))

#   The part where we make the computer do all the work!
    sphere_volume = (4/3) * math.pi * (sphere_radius ** 3)
    sphere_area = 4 * math.pi * (sphere_radius ** 2)

#   Output to user
    print()
    print(f"The radius given was: {sphere_radius}.")
    print(f"The volume of the sphere, V = 4/3πr³, rounded to {round_to} decimal places, is {sphere_volume:0.{round_to}f}.")
    print(f"The area of the sphere, A = 4πr², rounded to {round_to} decimal places, is {sphere_area:0.{round_to}f}.")

main()

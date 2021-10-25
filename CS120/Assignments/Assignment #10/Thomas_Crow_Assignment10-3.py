#   Assignment #10 Question #3
#
#   Thomas Crow
#   Date 10/23/2021
#
#   Requirements: Write a program that computes the intersection of a circle, which the radius is r and centered at (0,0), with a horizontal line, has 
#                 a intercept (0, y). Displays the information textually and graphically.
#
#                 Do it with a graphical user interface, and add a decision to handle the case where the line does not intersect the circle.
#
#                 Hint: x = ±√(r²-y²)

import math
from graphics import*

##################################################################################################################
#  Creates graphics window
#  Input: None
#  Output: A GraphWin object

def createWindow():
    win = GraphWin('Circle', 1000, 1000)
    win.setCoords(-20,-20,20,20)
    win.setBackground("white")
    return win

##################################################################################################################

##################################################################################################################
#  Description: 
#               
#
#  Input: None
#  Output: None

def computeIntersection():
    print("This program computes the intersection of a horizontal line segment with a circle.")



##################################################################################################################

def main():

    userWindow = createWindow()

#   Wait for user mouse click before closing window
    userWindow.getMouse()
    userWindow.close()

main()

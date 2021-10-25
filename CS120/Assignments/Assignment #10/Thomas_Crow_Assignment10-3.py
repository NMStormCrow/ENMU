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
from tkinter.constants import X
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
#  Creates a circle object
#  Input: None
#  Output: A circle object

def createCircle(win):

    circleCenter = Point(0,0)

    # Draw text boxes and entry button asking for radius
    radiusMessage=Text(Point(-10,18), "Please enter the radius:")
    radiusMessage.setSize(36)
    radiusMessage.setTextColor("black")
    radiusMessage.draw(win)

    # Create input box for user to input radius
    inputText=Entry(Point(0,18),2)
    inputText.setSize(36)
    inputText.setText("")
    inputText.setFill("white")
    inputText.draw(win)

    # Create a button for the user to click to enter radius value
    buttonBoxRadius=Rectangle(Point(4,17),Point(12,19))
    buttonBoxRadius.draw(win)
    buttonBoxRadius.setFill("grey")

    # Print text on the button to enter radius value
    buttonRadius=Text(Point(8,18), "Click Button")
    buttonRadius.setSize(36)
    buttonRadius.setTextColor("black")
    buttonRadius.draw(win)

    # Wait for user to click mouse.  This is necessary for getText() to work
    win.getMouse()

    # Remove unneeded buttons for cleaner UI
    buttonRadius.undraw()
    buttonBoxRadius.undraw()
    radiusMessage.undraw()
    inputText.undraw()

    # Record the inputed text and output to user
    Radius=float(inputText.getText())

    newCircle = Circle(circleCenter, Radius)
    newCircle.setFill("blue")

    
    return newCircle, Radius

##################################################################################################################

##################################################################################################################
#  Creates a line object
#  Input: None
#  Output: A line object, the y-intercept

def createLine(win):
    
    # Draw text boxes and entry button asking for radius
    yInterceptMessage=Text(Point(-2,18), "Please enter the y-intercept of the horizontal line at x=0: ")
    yInterceptMessage.setSize(36)
    yInterceptMessage.setTextColor("black")
    yInterceptMessage.draw(win)

    # Create input box for user to input radius
    inputText=Entry(Point(18,18),2)
    inputText.setSize(36)
    inputText.setText("")
    inputText.setFill("white")
    inputText.draw(win)

    # Create a button for the user to click to enter radius value
    buttonBoxyIntercept=Rectangle(Point(4,15),Point(12,17))
    buttonBoxyIntercept.draw(win)
    buttonBoxyIntercept.setFill("grey")

    # Print text on the button to enter radius value
    buttonyIntercept=Text(Point(8,16), "Click Button")
    buttonyIntercept.setSize(36)
    buttonyIntercept.setTextColor("black")
    buttonyIntercept.draw(win)

    # Wait for user to click mouse.  This is necessary for getText() to work
    win.getMouse()

    # Remove unneeded buttons for cleaner UI
    buttonBoxyIntercept.undraw()
    buttonyIntercept.undraw()
    yInterceptMessage.undraw()
    inputText.undraw()


    # Record the inputed text and output to user
    yIntercept=float(inputText.getText())

    newLineLeftPoint = Point(-20, yIntercept)
    newLineRightPoint = Point(20, yIntercept)
    newLine = Line(newLineLeftPoint,newLineRightPoint)
    newLine.setWidth(3)
    return newLine, yIntercept

##################################################################################################################

##################################################################################################################
#  Create x-axis
#  Input: None
#  Output: A line object

def createXAxis():
    xAxisLeftPoint = Point(-20,0)
    xAxisRightPoint = Point(20, 0)
    xAxis = Line(xAxisLeftPoint,xAxisRightPoint)
    xAxis.setWidth(1)
    return xAxis

##################################################################################################################

##################################################################################################################
#  Create y-axis
#  Input: None
#  Output: A line object

def createYAxis():
    yAxisTopPoint = Point(0,20)
    yAxisBottomPoint = Point(0,-20)
    yAxis = Line(yAxisTopPoint,yAxisBottomPoint)
    yAxis.setWidth(1)
    return yAxis

##################################################################################################################

##################################################################################################################
#  Description: 
#               
#
#  Input:  The radius of the circle, the y-intercept of the horizontal line
#  Output: None
#
#


def computeIntersection(radius, yIntercept, win):
    
    if (abs(yIntercept) > (radius)):
        thirdString = "The line does not intercept the circle."
        
    else:
        xIntercept = round(math.sqrt((radius ** 2) - (yIntercept ** 2)),2)
        thirdString = "The X-Intercepts of the line and the circle is: " + str(xIntercept) + " and " + str(-(xIntercept))

    firstString = "The radius of the circle is: " + str(radius)
    secondString = "The Y-Intercept of the horizontal line is: " + str(yIntercept)


    firstInterceptMessage=Text(Point(-2,18), firstString)
    firstInterceptMessage.setSize(36)
    firstInterceptMessage.setTextColor("black")
    firstInterceptMessage.draw(win)

    secondInterceptMessage=Text(Point(-2,16), secondString)
    secondInterceptMessage.setSize(36)
    secondInterceptMessage.setTextColor("black")
    secondInterceptMessage.draw(win)

    thirdInterceptMessage=Text(Point(0,14), thirdString)
    thirdInterceptMessage.setSize(36)
    thirdInterceptMessage.setTextColor("black")
    thirdInterceptMessage.draw(win)




##################################################################################################################

def main():

    userWindow = createWindow()
    userCircle, userRadius = createCircle(userWindow)
    userLine, userYintercept = createLine(userWindow)
    computeIntersection(userRadius,userYintercept, userWindow)
    
    x_axis = createXAxis()
    x_axis.draw(userWindow)
    y_axis = createYAxis()
    y_axis.draw(userWindow)
    userCircle.draw(userWindow)
    userLine.draw(userWindow)

    # Wait for user mouse click before closing window
    userWindow.getMouse()
    userWindow.close()




main()

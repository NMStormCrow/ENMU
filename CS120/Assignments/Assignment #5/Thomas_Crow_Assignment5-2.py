# Assignment #5 Question #2
#
# Thomas Crow
# Date 9/19/2021
#
# Requirements:
#
# 2. Write a program that computes the intersection of a circle with a horizontal line and displays
#    the information textually and graphically. Do it with a graphical user interface.
#
#    You can complete this question with the following steps
#
#    1). Draw a circle centered at (0, 0) with the given radius, r, in a window with coordinates
#        running from -10,-10 to 10, 10.
#
#    2). Draw a horizontal line across the window with the given y-intercept.
#
#    3). Draw the two points of intersection in red.
#
#    4). Print out the x values of the points of intersection.
#
#    Hint: the formula to calculate the intersections
#          x = +/- sqrt(r^2 - y^2)
#
#


import math
from graphics import*

def main():

    # Create graphics window named Circle and Line
    win=GraphWin('Circle and Line', 1000, 1000)
    win.setCoords(-10, -10, 10, 10)

    # Define background
    win.setBackground("white")

    # Draw text boxes and entry button asking for radius
    radiusMessage=Text(Point(-6,9), "Please enter the radius:")
    radiusMessage.setSize(36)
    radiusMessage.setTextColor("black")
    radiusMessage.draw(win)

    # Create input box for user to input radius
    inputText=Entry(Point(-1.8,9),2)
    inputText.setSize(36)
    inputText.setText("")
    inputText.setFill("cyan")
    inputText.draw(win)

    # Create a button for the user to click to enter radius value
    buttonBoxRadius=Rectangle(Point(1,8.6),Point(5,9.4))
    buttonBoxRadius.draw(win)
    buttonBoxRadius.setFill("grey")

    # Print text on the button to enter radius value
    buttonRadius=Text(Point(3,9), "Click Button")
    buttonRadius.setSize(36)
    buttonRadius.setTextColor("black")
    buttonRadius.draw(win)

    # Wait for user to click mouse.  This is necessary for getText() to work
    win.getMouse()

    # Remove unneeded buttons for cleaner UI
    buttonRadius.undraw()
    buttonBoxRadius.undraw()
    radiusMessage.undraw()

    # Record the inputed text and output to user
    myCircleRadius=float(inputText.getText())
    radiusMessageString="The given radius is: " + str(myCircleRadius)
    radiusMessage.setText(radiusMessageString)
    radiusMessage.move(-0.2,0)
    radiusMessage.draw(win)

    # Create and draw circle with the center of (0,0) and a radius specified by user
    centerMyCircle=Point(0,0)
    MyCircle=Circle(centerMyCircle,myCircleRadius)
    MyCircle.draw(win)
    MyCircle.setFill("blue")

    # Draw text boxes and entry button asking for y-intercept
    yinterceptMessage=Text(Point(-5.325,8), "Please enter the y-intercept:")
    yinterceptMessage.setSize(36)
    yinterceptMessage.setTextColor("black")
    yinterceptMessage.draw(win)

    # Create input box for user to input y-intercept
    inputText.move(1.4,-1)
    inputText.setText("")

    # Create a button for the user to click to enter y-intercept value
    yinterceptButtonBox=Rectangle(Point(1,7.6),Point(5,8.4))
    yinterceptButtonBox.draw(win)
    yinterceptButtonBox.setFill("grey")

    # Print text on the button to enter y-intercept value
    yinterceptButton=Text(Point(3,8), "Click Button")
    yinterceptButton.setSize(36)
    yinterceptButton.setTextColor("black")
    yinterceptButton.draw(win)

    # Wait for user to click mouse.  This is necessary for getText() to work
    win.getMouse()

    # Remove unneeded buttons for cleaner UI
    yinterceptMessage.undraw()
    yinterceptButtonBox.undraw()
    yinterceptButton.undraw()
    inputText.undraw()

    # Recorded the inputed text and output to user
    yintercept=float(inputText.getText())
    yinterceptMessageString="The given y-intercept is: " + str(yintercept)
    yinterceptMessage.setText(yinterceptMessageString)
    yinterceptMessage.move(-0.2,0)
    yinterceptMessage.draw(win)

    # Draw horizontal line at y-yinterceptButton
    horizontalLineStart=Point(-10,yintercept)
    horizontalLineEnd=Point(10,yintercept)
    horizontalLine=Line(horizontalLineStart,horizontalLineEnd)
    horizontalLine.setWidth(4)
    horizontalLine.draw(win)

    # Determine x-axis
    firstIntercept=math.sqrt((myCircleRadius ** 2) - (yintercept ** 2))
    secondIntercept=-abs(firstIntercept)

    # Draw intercept circles
    firstInterceptCircleCenter=Point(firstIntercept,yintercept)
    firstInterceptCircle=Circle(firstInterceptCircleCenter,(myCircleRadius * 0.1))
    firstInterceptCircle.draw(win)
    firstInterceptCircle.setFill("red")

    secondInterceptCircleCenter=Point(secondIntercept,yintercept)
    secondInterceptCircle=Circle(secondInterceptCircleCenter,(myCircleRadius * 0.1))
    secondInterceptCircle.draw(win)
    secondInterceptCircle.setFill("red")

    # Print out the x-axis values of the intercepts
    firstInterceptMessageString="The first x-axis value of the intercepts is: " + (str(round(firstIntercept,2)))
    firstInterceptMessage=Text(Point(-2.68,-8), firstInterceptMessageString)
    firstInterceptMessage.setSize(36)
    firstInterceptMessage.setTextColor("black")
    firstInterceptMessage.draw(win)

    secondInterceptMessageString="The second x-axis value of the intercepts is: " + (str(round(secondIntercept,2)))
    secondInterceptMessage=Text(Point(-2,-9), secondInterceptMessageString)
    secondInterceptMessage.setSize(36)
    secondInterceptMessage.setTextColor("black")
    secondInterceptMessage.draw(win)

    win.getMouse()  # Wait for mouse-click before closing window
    win.close() # Closes window

main()

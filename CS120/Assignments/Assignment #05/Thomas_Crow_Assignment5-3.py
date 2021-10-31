# Assignment #5 Question #3
#
# Thomas Crow
# Date 9/19/2021
#
# Requirements:
#
#  3. Modify the program of class example (circle moves), do the following tasks
#
#  (a) Make it draw squares instead of circles.
#
#  (b) Have each successive click draw an additional square on the screen(rather than moving the existing one).
#
#  (c) Print a message on the window "Click again to quit" after the loop, and wait for a final click before closing the window.
#
#


import math
from graphics import*

def main():

    # Create graphics window named Circle and Line
    win=GraphWin('Circle and Line', 1000, 1000)
    win.setBackground("black")
    win.setCoords(-100, -100, 100, 100)

    # Draw first square
    userSquare=Rectangle(Point(0,0),Point(30,30))
    userSquare.setOutline("white")
    userSquare.setFill("white")
    userSquare.draw(win)

    # Loop to repeat drawing a square based on the location of the user mouse click 5 times
    for i in range(5):
        userPoint=win.getMouse()
        firstPoint=Point((userPoint.getX()-15),(userPoint.getY()-15))
        secondPoint=Point((userPoint.getX()+15),(userPoint.getY()+15))
        userSquare=Rectangle(firstPoint,secondPoint)
        userSquare.setOutline("white")
        userSquare.setFill("white")
        userSquare.draw(win)

    # Create a button for the user to click to quit application
    buttonBoxRadius=Rectangle(Point(-80,-80),Point(-20,-90))
    buttonBoxRadius.draw(win)
    buttonBoxRadius.setFill("white")

    # Print text on the button to quit application
    buttonRadius=Text(Point(-50,-85), "Click again to quit")
    buttonRadius.setSize(36)
    buttonRadius.setTextColor("black")
    buttonRadius.draw(win)

    # Wait for user mouse click before finishing
    win.getMouse()  # Wait for mouse-click before closing window
    win.close() # Closes window

main()

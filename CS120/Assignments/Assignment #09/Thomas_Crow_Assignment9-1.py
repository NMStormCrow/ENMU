#   Assignment #9 Question #1
#
#   Thomas Crow
#   Date 10/17/2021
#
#   Requirements:
#
#   Write a function to meet this specification.
#   moveTo (shape, newCenter) shape is a graphics object that supports the getCenter method and newCenter is a Point.
#   Moves shape so that newCenter is its center.

#   Use your function to write a program that draws a circle and then allows the user to click the window 10 times.
#   Each time the user clicks, the circle is moved where the user clicked.

from graphics import*

##################################################################################################################
#  Creates graphics window
#  Input: None
#  Output: A GraphWin object

def createWindow():
    win = GraphWin('Movable Circle', 1000, 1000)
    win.setCoords(-10,-10,10,10)
    win.setBackground("black")
    return win

##################################################################################################################
#  Creates a circle object
#  Input: None
#  Output: A circle object

def createCircle():
    newCircleCenter = Point(0,0)
    newCircle = Circle(newCircleCenter, 3)
    newCircle.setFill("red")
    return newCircle

##################################################################################################################
#  Moves The circle to the point mouse clicked by user
#  Input: A circle objetct, a point object
#  Output: A circle object

def moveTo(shape, newCenter):
    shape.undraw()
    newCircle = Circle(newCenter, 3)
    newCircle.setFill("red")
    return newCircle

##################################################################################################################


def main():

#   Create the graphical window and the initial default circle
    userWindow = createWindow()
    userCircle = createCircle()
    userCircle.draw(userWindow)

#   Loop the user clicking and creating a new circle on the spot of the mouse click ten times
    for i in range(10):
        userPoint = userWindow.getMouse()
        userCircle.undraw()
        userCircle = moveTo(userCircle,userPoint)
        userCircle.draw(userWindow)

#   Wait for user mouse click before closing window
    userWindow.getMouse()
    userWindow.close()

main()

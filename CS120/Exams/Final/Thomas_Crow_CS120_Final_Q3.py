#  CS 120 Final Question #3
#  Thomas Crow

# Write a Python program that reads two circles and then determines whether they overlap or not. Note that a circle will be represented by its center (cx, cy) and radius r. Note that when circles meet at only one point, we still consider that as overlapping.
# Draw the circles and intersections if have in the window.
# Note: Consider all different cases.

from graphics import*
import math

def determineIfCirclesIntersect():

    win=GraphWin('Circles', 1000, 1000)
    win.setCoords(-10, -10, 10, 10)
    win.setBackground("white")

    firstCircleCenterX = eval(input("Please enter the x value for the center of the first circle: "))
    firstCircleCenterY = eval(input("Please enter the y value for the center of the first circle: "))
    firstCircleRadius = eval(input("Please enter the radius of the first circle: "))
    firstradius = firstCircleRadius
    firstCircleCenter = Point(firstCircleCenterX,firstCircleCenterY)
    firstCircle = Circle(firstCircleCenter, firstCircleRadius)

    secondCircleCenterX = eval(input("Please enter the x value for the center of the second circle: "))
    secondCircleCenterY = eval(input("Please enter the y value for the center of the second circle: "))
    secondCircleRadius = eval(input("Please enter the radius of the second circle: "))
    secondradius = secondCircleRadius
    secondCircleCenter = Point(secondCircleCenterX,secondCircleCenterY)
    secondCircle = Circle(secondCircleCenter, secondCircleRadius)

    distance = math.sqrt((secondCircleCenterX - firstCircleCenterX) ** 2 + (secondCircleCenterY - firstCircleCenterY) ** 2 )



    firstCircle.draw(win)
    secondCircle.draw(win)
    firstCircle.setFill("red")
    secondCircle.setFill("blue")

    if (distance < (firstradius - secondradius)) or (distance < (secondradius - firstradius)) or (distance > (firstradius + secondradius)):
        textbox = Text(Point(-5.325,8), "The circles overlap")
    else:
        textbox = Text(Point(-5.325,8), "The circles do not overlap")
    textbox.setSize(36)
    textbox.setTextColor("black")
    textbox.draw(win)


    win.getMouse()





def main():
    determineIfCirclesIntersect()



main()
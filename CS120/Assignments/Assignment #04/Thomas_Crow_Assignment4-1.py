# Assignment #4 Question #1
#
# Thomas Crow
# Date 9/11/2021
#
# Requirements:
# An archery target consists of a central circle of yellow surrounded by concentric rings of red, blue, black and white.
# Each ring has the same width, which is the same as the radius of the yellow circle. Write a program that draws such a target.
#
# Hint:
# Objects drawn later will appear on top of objects drawn earlier.
#

from graphics import*

def main():

    # Define background
    background=Rectangle(Point(0,0),Point(200,200))

    # Define size of each circle
    center=Point(100,100)  # Defines the center of the circles
    whiteCirc=Circle(center,75)
    blackCirc=Circle(center,60)
    blueCirc=Circle(center,45)
    redCirc=Circle(center,30)
    yellowCirc=Circle(center,15)

    # Define the bullseye
    bullseye=Text(center,"+")

    # Create graphics window named Archery Target
    win=GraphWin('Archery Target')

    # Draw background
    background.draw(win)
    background.setFill("cyan")

    #  Draw and fill each circle of archery target
    whiteCirc.draw(win)
    whiteCirc.setFill("white")
    blackCirc.draw(win)
    blackCirc.setFill("black")
    blueCirc.draw(win)
    blueCirc.setFill("blue")
    redCirc.draw(win)
    redCirc.setFill("red")
    yellowCirc.draw(win)
    yellowCirc.setFill("yellow")
    bullseye.draw(win)

    win.getMouse()  # Wait for mouse-click before closing window
    win.close() # Closes window

main()

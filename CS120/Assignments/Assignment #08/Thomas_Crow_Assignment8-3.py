# Assignment #8 Question #3
#
# Thomas Crow
# Date 10/10/2021
#
#   Requirements:
#
#   Write and test a function to meet this specification. drawFace (center, size, win) center is a Point, size is an int, and win is a GraphWin. Draws a simple face of the given size in win. Your function can draw a simple smiley (or grim) face.
#
#   Demonstrate the function by writing a program that draws several faces of varying size in a single window.
#
#

from graphics import*

##################################################################################################################
#  Draws a simple face with the given size in win
#  Input: center is a point that will be the center of a Circle
#         size is an int that
#         win
#  Output: None

def drawJackoLantern(center, size, win):

    JackoLantern = Circle(center, size)
    JackoLantern.draw(win)
    JackoLantern.setFill("orange")

    JackoLanternLeftEyePointA=Point(center.getX()-(size * 0.1),(center.getY()+(size * 0.3)))
    JackoLanternLeftEyePointB=Point((JackoLanternLeftEyePointA.getX() - (size * 0.6)),(JackoLanternLeftEyePointA.getY()))
    JackoLanternLeftEyePointC=Point(JackoLanternLeftEyePointA.getX()-(size * 0.3),JackoLanternLeftEyePointA.getY()+(size * 0.4))
    JackoLanternLeftEye=Polygon(JackoLanternLeftEyePointA,JackoLanternLeftEyePointB,JackoLanternLeftEyePointC)


    JackoLanternRightEye=JackoLanternLeftEye.clone()
    JackoLanternRightEye.move(size * 0.8,0)


    JackoLanternNosePointA=Point(center.getX()+(size * 0.2),(center.getY()-(size * 0.2)))
    JackoLanternNosePointB=Point(center.getX()-(size * 0.2),JackoLanternNosePointA.getY())
    JackoLanternNosePointC=Point(center.getX(),JackoLanternNosePointA.getY()+(size * 0.4))
    JackoLanternNose=Polygon(JackoLanternNosePointA,JackoLanternNosePointB,JackoLanternNosePointC)

    JackoLanternMouthPointA=Point(center.getX()-(size*0.5),center.getY()-(size * 0.75))
    JackoLanternMouthPointB=Point(center.getX()+(size*0.5),center.getY()-(size * 0.4))
    JackoLanternMouth=Oval(JackoLanternMouthPointA,JackoLanternMouthPointB)

    JackoLanternLeftEye.draw(win)
    JackoLanternLeftEye.setFill("black")
    JackoLanternRightEye.draw(win)
    JackoLanternRightEye.setFill("black")
    JackoLanternNose.draw(win)
    JackoLanternNose.setFill("black")
    JackoLanternMouth.setOutline("black")
    JackoLanternMouth.setFill("yellow")
    JackoLanternMouth.setWidth(10)
    JackoLanternMouth.draw(win)



    win.getMouse()  # Wait for mouse-click before closing window
    win.close() # Closes window

##################################################################################################################

##################################################################################################################
#  Draws a Jack o Lantern with a small size
#  Input: None
#  Output: None

def SmallJackoLantern():

    SmallJackoLanternCenter = Point(-3,3)
    SmallJackoLanternSize= 3
    SmallJackoLantern=GraphWin('JackoLantern',1000,1000)
    SmallJackoLantern.setBackground("black")
    SmallJackoLantern.setCoords(-10, -10, 10, 10)
    drawJackoLantern(SmallJackoLanternCenter,SmallJackoLanternSize,SmallJackoLantern)
##################################################################################################################

##################################################################################################################
#  Draws a Jack o Lantern with a medium size
#  Input: None
#  Output: None

def MediumJackoLantern():

    MediumJackoLanternCenter = Point(3,-3)
    MediumJackoLanternSize= 6
    MediumJackoLantern=GraphWin('JackoLantern',1000,1000)
    MediumJackoLantern.setBackground("black")
    MediumJackoLantern.setCoords(-10, -10, 10, 10)
    drawJackoLantern(MediumJackoLanternCenter,MediumJackoLanternSize,MediumJackoLantern)
##################################################################################################################

##################################################################################################################
#  Draws a Jack o Lantern with a large size
#  Input: None
#  Output: None

def LargeJackoLantern():

    LargeJackoLanternCenter = Point(0,0)
    LargeJackoLanternSize= 9
    LargeJackoLantern=GraphWin('JackoLantern',1000,1000)
    LargeJackoLantern.setBackground("black")
    LargeJackoLantern.setCoords(-10, -10, 10, 10)
    drawJackoLantern(LargeJackoLanternCenter,LargeJackoLanternSize,LargeJackoLantern)
##################################################################################################################




def main():

    SmallJackoLantern()
    MediumJackoLantern()
    LargeJackoLantern()

main()

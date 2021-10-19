# Assignment #5 Question #1
#
# Thomas Crow
# Date 9/19/2021
#
# Requirements:
#
# Write a program that click five times to draw some sort of face.
#
# There are 5 "control points" for the face that come from 5 mouse clicks by the user.
#
# In order they are:
# p1: The center of the face
# p2: Somewhere on the edge of the face
# p3: The lower-left corner of the nose
# p4: The center of the left eye
# p5: The lower-left corner of the mouth
#
# The size and locations of the various features are determined by these control points as follows:
#
# Head: This is a circle centered at p1 and having radius equal to the distance from p1 to p2.
#
# Nose: The nose is an isosceles triangle formed by p1, p3, and a point that is vertically aligned with p3 and the same distance to the right of p1 as p3 is to the left of p1.
#       Thus the nose will always be symmetric and horizontally centered in the face.
#
# Eyes: The eyes are circles with a radius equal to one-tenth the radius of the head. The left eye is centered at p4 and the right eye should be placed symmetrically to match the left.
#
# Mouth: The mouth is an oval with the lower-left corner of its bounding-box at p5. The mouth is centered horizontally and the height of the bounding-box is the same as the
#        radius of the eyes
#


import math
from graphics import*

def main():

    # Create graphics window named Dynamic Head
    win=GraphWin('Dynamic Head', 1000, 1000)

    # Define background
    win.setBackground("black")

    # Define location, size of the head and draw
    centerHead=win.getMouse() # Defines the center of the circle that will be the head
    edgepointHead=win.getMouse() # Define the edge of the circle that will be the head
    radiusHead=math.sqrt(((edgepointHead.getX() - centerHead.getX()) ** 2) + ((edgepointHead.getY() - centerHead.getY()) ** 2)) # Determine the radius using sqrt((x2-x1)^2 + (y2-y1)^2)
    dynamicHead=Circle(centerHead, radiusHead)
    dynamicHead.draw(win)
    dynamicHead.setFill("blue")

    # Define location, size of the nose and draw
    edgepointNose=win.getMouse() # Define the edge of the triangle that will be the nose
    widthNose=(centerHead.getX() - edgepointNose.getX()) # Determine the distance on the X axis between the corner of the triangle and the center of the face
    clonepointNose=Point(edgepointNose.getX() + (2 * widthNose), edgepointNose.getY()) # Create point with x-axis the same distance past the center of the face, same y-axis value
    dynamicNose=Polygon(centerHead,edgepointNose,clonepointNose) # Create triangle that will have the three points created above. This will be the nose
    dynamicNose.draw(win)
    dynamicNose.setFill("black")

    # Define size, location of the eyes and draw
    centerLeftEye=win.getMouse() # Define the center of the left eye
    distanceEyes=(centerHead.getX() - centerLeftEye.getX()) # Determine the distance on the x-axis from the center of the face to the center of the left eye
    radiusEyes=(0.1 * dynamicHead.getRadius()) # Set the radius of the eyes to 1/10th the radius of the face
    dynamicLeftEye=Circle(centerLeftEye,radiusEyes) # Create circle with the center point and radius above. This will be the left eye.
    dynamicRightEye=dynamicLeftEye.clone() #  Create clone of circle above. This will be the right eye
    dynamicRightEye.move(2 * distanceEyes, 0) #  Move right eye on x-axis to my symmetric with left eye
    dynamicLeftEye.draw(win)
    dynamicLeftEye.setFill("black")
    dynamicRightEye.draw(win)
    dynamicRightEye.setFill("black")

    # Define size, location of the mouth and draw
    edgepointMouth=win.getMouse() # Define edge point of Mouth
    distanceMouth=(centerHead.getX() - edgepointMouth.getX()) # Determine the distance on the x-axis from the center of the face to the edge of the mouth
    oppositepointMouth=Point((edgepointMouth.getX() + (2 * distanceMouth)), (edgepointMouth.getY() + radiusEyes)) # Determine the opposite end of the mouth
    dynamicMouth=Oval(edgepointMouth,oppositepointMouth) # Create an oval using the two points above
    dynamicMouth.draw(win)
    dynamicMouth.setFill("black")

    win.getMouse()  # Wait for mouse-click before closing window
    win.close() # Closes window

main()

# Assignment #4 Question #2
#
# Thomas Crow
# Date 9/11/2021
#
# Requirements:
#
# Write a (smurfy) program that draws some sort of face like the following.
#

from graphics import*

def main():

    center=Point(100,100)  # Defines the center of the circles

    # Define background
    background=Rectangle(Point(0,0),Point(200,200))

    # Define size of the smurf's smurfHead
    smurfHead=Circle(center,50)

    # Define size and shape of the smurf's hat
    smurfHatA=Point(50,75)
    smurfHatB=Point(100,25)
    smurfHatC=Point(150,25)
    smurfHatD=Point(150,50)
    smurfHatE=Point(125,50)
    smurfHatF=Point(150,75)
    smurfHat=Polygon(smurfHatA,smurfHatB,smurfHatC,smurfHatD,smurfHatE,smurfHatF)

    # Define the size and shape of the smurf's eyes
    smurfRightEyeCenter=Point(80,80)
    smurfRightEyeVertex=Point(100,105)
    smurfRightEye=Oval(smurfRightEyeCenter,smurfRightEyeVertex)
    smurfLeftEye=smurfRightEye.clone()
    smurfLeftEye.move(20,0)

    # Define the size and shape of the smurf's pupils
    smurfRightPupilCenter=Point(90,100)
    smurfRightPupil=Circle(smurfRightPupilCenter,5)
    smurfLeftPupil=smurfRightPupil.clone()
    smurfLeftPupil.move(20,0)

    # Define the size and shape of the smurf's nose
    smurfNoseCenter=Point(100,110)
    smurfOuterNose=Circle(smurfNoseCenter,10)
    smurfInnerNose=Circle(smurfNoseCenter,8)

    # Define the size and shape of the smurf's smurfMouthA
    smurfMouth=Oval(Point(110,125),Point(85,140))

    # Create graphics window named Smurf
    win=GraphWin('Smurf')

    # Draw background
    background.draw(win)
    background.setFill("black")

    #  Draw and fill each smurf bodyparts
    smurfHead.draw(win)
    smurfHead.setFill("blue")

    smurfHat.draw(win)
    smurfHat.setFill("white")

    smurfRightEye.draw(win)
    smurfRightEye.setFill("white")

    smurfLeftEye.draw(win)
    smurfLeftEye.setFill("white")

    smurfRightPupil.draw(win)
    smurfRightPupil.setFill("black")

    smurfLeftPupil.draw(win)
    smurfLeftPupil.setFill("black")

    smurfOuterNose.draw(win)
    smurfOuterNose.setFill("black")

    smurfInnerNose.draw(win)
    smurfInnerNose.setFill("blue")

    smurfMouth.draw(win)
    smurfMouth.setFill("black")

    win.getMouse()  # Wait for mouse-click before closing window
    win.close() # Closes window

main()

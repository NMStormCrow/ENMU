#  CS 120 Exam 1 Question #2
#  Thomas Crow

from graphics import*

def main():

    win=GraphWin('Determine slope', 1000, 1000)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("white")

    firstPoint=win.getMouse()
    firstPointX=firstPoint.getX()
    firstPointY=firstPoint.getY()

    firstPointCircle=Circle(firstPoint, 0.05)
    firstPointCircle.draw(win)
    firstPointCircle.setFill("blue")

    secondPoint=win.getMouse()
    secondPointX=secondPoint.getX()
    secondPointY=secondPoint.getY()

    secondPointCircle=Circle(secondPoint,0.05)
    secondPointCircle.draw(win)
    secondPointCircle.setFill("blue")

    userSlope = ((secondPointY - firstPointY) / (secondPointX - firstPointX))

    userLine=Line(firstPoint,secondPoint)
    userLine.draw(win)
    userLine.setFill("black")

    textBox=Rectangle(Point(1,3),Point(9,1.25))
    textBox.draw(win)
    textBox.setFill("black")

    textBoxString = "The first point is: " + str(firstPoint)
    textBoxText=Text(Point(5,2.5), textBoxString)
    textBoxText.setSize(24)
    textBoxText.setTextColor("white")
    textBoxText.draw(win)

    textBoxString = "The second points is: " + str(secondPoint)
    textBoxText=Text(Point(5,2), textBoxString)
    textBoxText.setSize(24)
    textBoxText.setTextColor("white")
    textBoxText.draw(win)

    textBoxString = "The slope of the two points is: " + str(round(userSlope,2))
    textBoxText=Text(Point(5,1.5), textBoxString)
    textBoxText.setSize(24)
    textBoxText.setTextColor("white")
    textBoxText.draw(win)

    win.getMouse()

main()

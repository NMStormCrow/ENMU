#  CS 120 Exam 1 Question #3
#  Thomas Crow

from graphics import*

def main():

    win=GraphWin('Pretty Boxes', 1000, 1000)
    win.setCoords(0, 0, 10, 10)

    firstBox=Polygon(Point(0,0), Point(0,10), Point(10,10),Point(10,0))
    firstBox.draw(win)
    firstBox.setFill("red")

    secondBox=Polygon(Point(0,5), Point(5,10), Point(10,5), Point(5,0))
    secondBox.draw(win)
    secondBox.setFill("yellow")

    thirdBox=Polygon(Point(2.5,7.5), Point(7.5,7.5), Point(7.5,2.5), Point(2.5,2.5))
    thirdBox.draw(win)
    thirdBox.setFill("green")

    thirdBox=Polygon(Point(2.5,5), Point(5,7.5), Point(7.5,5), Point(5,2.5))
    thirdBox.draw(win)
    thirdBox.setFill("blue")


    win.getMouse()

main()

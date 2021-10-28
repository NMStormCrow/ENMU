#  CS 120 Exam 2 Question #1
#  Thomas Crow

from graphics import*
import math

def drawWindow():
    window = GraphWin('Circle', 750, 750)
    window.setCoords(-10,-10,10,10)
    window.setBackground("green")
    return window

def createRing(radius, color, window):
    center=Point(0,0)  # Defines the center of the circles
    circle=Circle(center, radius)
    circle.setFill(color)
    circle.draw(window)
    return circle

def scoreUserClick(window):
    
    center=Point(0,0)
    userClick = window.getMouse()
    distanceFromCenter = math.sqrt((userClick.getX()-center.getX()) ** 2 + (userClick.getY()-center.getY()) ** 2)
    if distanceFromCenter < 1:
        score = 9
    elif distanceFromCenter < 2:
        score = 7
    elif distanceFromCenter < 3:
        score = 5
    elif distanceFromCenter < 4:
        score = 3
    elif distanceFromCenter < 5:
        score = 1
    else:
        score = 0
    
    return score


def main():

    userWindow = drawWindow()
    whiteRing = createRing(5, "white", userWindow)
    blackRing = createRing(4, "black", userWindow)
    blackRing = createRing(3, "blue", userWindow)
    blackRing = createRing(2, "red", userWindow)
    blackRing = createRing(1, "yellow", userWindow)

    scoreSum = 0

    for i in range(5):
       scoreSum = scoreSum + scoreUserClick(userWindow)

    userWindow.getMouse()  # Wait for mouse-click before closing window
    userWindow.close() # Closes window

    print (f"The final score is: {scoreSum}")

main()
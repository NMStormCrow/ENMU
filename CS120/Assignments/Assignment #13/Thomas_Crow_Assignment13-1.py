#   Assignment #12 Question #1
#
#   Thomas Crow
#   Date 11/20/2021
#
#   Requirements:  Modify the cannonball simulation from the chapter so that it
#                  also calculates the maximum height acheived by the cannonball

from math import sin, cos, radians

class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        self.ymax = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1
        if (self.ypos > self.ymax):
            self.ymax = self.ypos
    
    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos

    def getYMax(self):
        return self.ymax

def getInputs():
    a = float (input ("Enter the launch angle (in degrees): "))
    v = float (input ("Enter the initial velocity (in meters/sec): "))
    h = float (input ("Enter the initial height (in meters): "))
    t = float (input ("Enter the time interval between position calculations: "))
    return a, v, h, t

def main():
    angle, vel, hO, time = getInputs()
    cball = Projectile(angle, vel, hO)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))
    print("Maximum height acheived: {0:0.1f} meters.".format(cball.getYMax()))

main()
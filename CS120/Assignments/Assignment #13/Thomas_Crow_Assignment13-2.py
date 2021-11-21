#   Assignment #12 Question #2
#
#   Thomas Crow
#   Date 11/20/2021
#
#   Requirements: Write a class to represent spheres. Your class should implement
#                 the following:
#
#                 __init__(self, radius) Creates a sphere with a given radius
#                 getRadius(self) Returns the radius of this sphere
#                 surfaceArea(self) Returns the surface area of the sphere
#                 volume(self) Returns the volume of the sphere
#
#                 Use your new class to calculate the volume and surface area of a
#                 sphere from its radius, given as inputs

import math

class Sphere:

    def __init__(self, radius):
        self.radius = radius
        self.surfaceArea = 4 * math.pi * (self.radius ** 2)
        self.volume = 4/3 * (math.pi ** 3) 

    def getRadius(self):
        return self.radius
    
    def surfaceArea(self):
        return self.surfaceArea
    
    def volume(self):
        return self.volume

def getInput():
    r = float (input ("Enter the radius of the sphere: "))
    return r
    
def main():
    sphereRadius = getInput()
    sphere = Sphere(sphereRadius)
    print("\nSphere radius: {0:0.1f}.".format(sphere.getRadius()))
    print("Sphere surface area: {0:0.1f}.".format(sphere.surfaceArea()))
    print("Sphere volume: {0:0.1f}.\n".format(sphere.volume()))

main()

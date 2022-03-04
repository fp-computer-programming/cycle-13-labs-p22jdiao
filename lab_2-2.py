# Author: JD 03/04/2022


def build_vehicel(w, a, d, c):
    # The variable will be equal to the coorisponding parameter
    wheels = w
    axels = a
    doors = d
    color = c
    return "There are {0} wheels, {1} axels, {2} doors, and the color is {3}".format(wheels,axels,doors,color)
# Input space
w1 = input("The number of wheels: ")
a1 = input("The number of the axels: ")
d1 = input("The number of doors: ")
c1 = input("The color of the car: ")
print(build_vehicel(w1, a1, d1, c1))
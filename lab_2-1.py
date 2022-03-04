# Author: JD 03/04/2022



def build_car():
    # Set all the variables equal to certain numbers
    wheels = 4
    axels = 2
    doors = 2
    color = "red"
    # Return the result as string.
    return "There are {0} wheels, {1} axels, {2} doors, and the color is {3}".format(wheels,axels,doors,color)



print(build_car())
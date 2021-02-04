# Author: Ileana Hernandez
# Date: 02/03/2021
# Description: Class named Taxicab with three private data members

class Taxicab():
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.odometer = 0     #initializes the odometer to zero

    def get_x_coord(self):  #get method for data member with x-coordinate
        return self.x_coordinate

    def get_y_coord(self):  #get method for data member with y-coordinate
        return self.y_coordinate

    def get_odometer(self):  #get method for data member with odometer
        return self.odometer

    def move_x(self, distance): #indicates how far Taxicab should shift left or right
        self.x_coordinate += distance
        self.odometer += abs(distance)

    def move_y(self, distance): #indicates how far Taxicab should shift up or down
        self.y_coordinate += distance
        self.odometer += abs(distance)


cab = Taxicab(5,-8)   # reates a Taxicab object at coordinates (5, -8)
cab.move_x(3)    #moves cab 3 units to the right
cab.move_y(-4)  #moves cab 4 units down
cab.move_x(-1)  #moves cab 1 unit left
print(cab.odometer)  #prints the current odometer reading



import math
class Line(object):
    def __init__(self,coord1,coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        #You can unpack the tuple by writing x1,y1=self.coord1 and that would have made the code more readable.
        dist = ((self.coord2[0]-self.coord1[0])**2) + ((self.coord2[1]-self.coord1[1])**2)
        dist = math.sqrt(dist)
        print('Distance = %1.10f' %(dist))

    def slope(self):
        slope = (self.coord1[1]-self.coord2[1])/(self.coord1[0]-self.coord2[0])
        print('Slope = %1.10f' % (slope))

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()
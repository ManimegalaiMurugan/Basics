import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coord1 = coor1
        self.coord2 = coor2
    
    def distance(self):
        return math.sqrt(pow(self.coord2[0]-self.coord1[0],2)+pow(self.coord2[1] - self.coord1[1],2))
    
    def slope(self):
        return ((self.coord2[1] - self.coord1[1])/(self.coord2[0]-self.coord1[0]))


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())

print(li.slope())

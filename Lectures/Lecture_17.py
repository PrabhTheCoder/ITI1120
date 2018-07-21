class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self,other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __ne__(self,other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_points(self):
        return (self.x,self.y)
    
#1. an obj of type point is created
#2. the address of that obj is stored in variable/parameter self
#3. calls__init__ method of that class


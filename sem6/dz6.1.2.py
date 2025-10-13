class Vector(object) :

    def __init__(self,x,y,z) :
        self.x=x
        self.y=y
        self.z=z
    def center(self,points):

        total = Vector(0, 0, 0)
        for point in points:
            total = total + point
        n = len(points)
        return total  / n

        
    

points = [Vector(1, 1, 1),Vector(3, 3, 3)]
print(center(points))

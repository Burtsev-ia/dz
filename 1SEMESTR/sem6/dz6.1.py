class Vector(object) :

    def __init__(self,x,y,z) :
        self.x=x
        self.y=y
        self.z=z
    def _abs_(self) :
        return ((self.x**2+self.y**2+self.z**2)**0.5)

    def __add__(self, a,b,c):
        return self.x + a, self.y + b, self.z + c
    def __sub__(self, a,b,c):
        return self.x - a, self.y - b, self.z - c
    def __mul__(self,a,b,c):
        return self.x * a +self.y * b+ self.z * c
    def _chislo_(self,m):
        return self.x * m, self.y * m, self.z * m
    

c=Vector(1,1,1)
print(c.__add__(1,1,1))

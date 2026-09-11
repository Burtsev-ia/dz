class Vector(object) :

    def __init__(self,x,y,z) :
        self.x=x
        self.y=y
        self.z=z
    def triangle(p1, p2, p3):
        side1 = p2 - p1
        side2 = p3 - p1
    
        cross_x = side1.y * side2.z - side1.z * side2.y
        cross_y = side1.z * side2.x - side1.x * side2.z
        cross_z = side1.x * side2.y - side1.y * side2.x

        cross_magnitude = math.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        return cross_magnitude / 2.0

    def max_triangle(points):
    
        max_area = 0
        best_points = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    p1, p2, p3 = points[i], points[j], points[k]
                    area = triangle_area(p1, p2, p3)
                    if area > max_area:
                        max_area = area
                        best_points = (p1, p2, p3)
    
        return (max_area,) + best_points if best_points else (0, None, None, None)



        
    

points = [Vector(1, 1, 1),Vector(3, 3, 3),Vector(4,4,4)]
print(max_triangle(points))

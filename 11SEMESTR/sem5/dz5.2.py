import math
r,k=list(map(float,input().split()))
print('лина окружности равно',round(math.pi*2*r,2),'. Площадь круга составляет',round((math.pi*r**2)/k**2*100,2),'% от площади квадрата.')

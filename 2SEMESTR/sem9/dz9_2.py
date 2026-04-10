import math

r, kv =list(map(int, input().split()))
lr = (math.pi * 2 * r)
sr = math.pi * r ** 2
skv = kv ** 2
proc = sr / skv * 100
print(f'Длина окружности равно {lr:.2f}.Площадь круга составляет {proc:.2f}% \
от площади квадрата.')

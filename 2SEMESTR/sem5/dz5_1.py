import math
# from itertools import permutations
from itertools import combinations


n = int(input())
points = list()
for _ in range(n):
    i, j = list(map(float, input().split()))
    points.append([i, j])
print(points)
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(0.0)
        else:
            dist = math.sqrt((points[j][0]
                              - points[i][0])**2
                             + (points[j][1] - points[i][1])**2)
            row.append(dist)
    matrix.append(row)
print(matrix)
paths = list()
for i in range(1, n-1):
    paths.extend(list(combinations(list(range(2, n)), i)))
p = list()
for i in paths:
    v = list()
    v.append(0)
    v.extend(list(i))
    v.append(1)
    p.append(v)
print(p)
maxies = list()
for i in p:
    maxi = -1
    li = list()
    for j in range(len(i) - 1):
        li.append([i[j], i[j+1]])
    for k1, k2 in li:
        maxi = max(maxi, matrix[k1][k2])
    maxies.append(maxi)
    # print(li)
print(round(min(maxies), 3))

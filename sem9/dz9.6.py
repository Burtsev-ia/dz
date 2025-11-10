import heapq
a = list(map(int, input().split()))
"""n = len(a)
for i in range(n):
    a[i] *= (-1)"""
heapq.heapify(a)
"""for i in range(n):
    a[i] *= (-1)"""
print(a)

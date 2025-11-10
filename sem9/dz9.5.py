import heapq
a = list(map(int, input().split()))
heapq.heapify(a)
def heapsort(x):
    l = len(x)
    for i in range(l):
        x[0], x[l-1-i] = x[l-1-i], x[0]
        heapq._siftdown(a, 0, 1)
print(heapsort(a))
        

import heapq
a = list(map(int, input().split()))
heapq.heapify(a)


def heapsort(x):
    p = len(x)
    for i in range(p):
        # print('1')
        x[0], x[p-1-i] = x[p-1-i], x[0]
        heapq._siftup(x, 0)
        # print(x)
    return x


print(heapsort(a))

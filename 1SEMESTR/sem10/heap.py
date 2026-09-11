'''Этот pep8 требует переименовать все функции из примера
потому что якобы не должны в них Uppers быть
короче я не буду такой хренью заниматься
тем более что это не моя часть кода
'''


class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * 1e10  # or sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        return pos * 2 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
               self.Heap[pos] > self.Heap[self.rightChild(pos)]):
                if self.Heap[self.leftChild(pos)]\
                   < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def print_heap(self):
        print(self.Heap[1:])

    def remove_head(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped

    def mirror(self):
        co = 0
        while 2 ** co <= self.size:
            co += 1
        # print(co)
        for i in range(2, co + 1):
            if 2 ** i <= self.size:
                a = self.Heap[2 ** (i-1):2 ** i]
                self.Heap[2 ** (i-1):2 ** i] = a[::-1]
                # print(a[::-1])
            else:
                a = self.Heap[2 ** (i-1):2 ** i]
                self.Heap[2 ** (i-1):2 ** i] = a[::-1]
                # print(a[::-1])
                break

    def predki(self, i):
        # отсчет i начинается с нуля
        a = self.Heap[1:]
        while i != 0:
            i = (i-1) // 2
            print(a[i])

    def is_mirror(self):
        co = 0
        b = list()
        b.append(self.Heap[1])
        while 2 ** co <= self.size:
            co += 1
        for i in range(2, co + 1):
            # print(self.Heap[1])
            if 2 ** i <= self.size:
                a = self.Heap[2 ** (i-1):2 ** i]
                # self.Heap[2 ** (i-1):2 ** i] = a[::-1]
                # print(a[::-1])
                # b.append(a[::-1])
                for k in a[::-1]:
                    b.append(k)
            else:
                a = self.Heap[2 ** (i-1):2 ** i]
                # self.Heap[2 ** (i-1):2 ** i] = a[::-1]
                # print(a[::-1])
                # b.append(a[::-1])
                for k in a[::-1]:
                    b.append(k)
                break
        # print(b)
        # print(self.Heap[1:])
        g = self.Heap[::-1]
        # print(self.Heap[::-1])
        for i in range(len(self.Heap[1:])):
            if g[0] != 0:
                # print('l')
                break
            if g[0] == 0:
                # print('ff')
                # print(i)
                g.pop(0)
        # print(g)
        g = g[::-1]
        g = g[1:]
        if b == g:
            print('это зеркальное дерево')
        else:
            print('это лабуда')


print('The minHeap is ')
minHeap = MinHeap(15)
minHeap.insert(3)
minHeap.insert(5)
minHeap.insert(5)
minHeap.insert(6)
minHeap.insert(7)
minHeap.insert(7)
minHeap.insert(6)
# minHeap.insert(69)
minHeap.is_mirror()
print('-------')
'''minHeap.insert(5)
minHeap.insert(3)
minHeap.insert(17)
minHeap.insert(10)
minHeap.insert(84)
minHeap.insert(19)
minHeap.insert(6)
minHeap.insert(22)
minHeap.insert(9)
minHeap.insert(999)
'''
# minHeap.predki(6)
minHeap.print_heap()
# minHeap.minHeap()
minHeap.mirror()
# minHeap.minHeap()
print('-----')
minHeap.print_heap()

import random
a=[random.randrange(0, 1000, 10) for _ in range(100)]
b=[random.randrange(0, 1000, 10) for _ in range(100)]
print(set(a),end='\n\n\n\n')
print(set(b),end='\n\n\n\n')
a1=set(a)
b1=set(b)
print(a1|b1,end='\n\n\n\n')
print(a1&b1,end='\n\n\n\n')

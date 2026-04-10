a = input()
if len(a) < 4:
    co = 0
    for i in a:
        if i.islower():
            co += 1
    if co == 0:
        print(a.upper())
    else:
        print(a)
else:
    co = 0
    for i in a[:4]:
        if i.isupper():
            co += 1
    if co <= 1:
        print(a)
    else:
        print(a.upper())
            

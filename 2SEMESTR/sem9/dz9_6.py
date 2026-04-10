a = input()
if len(a) <= 2:
    print(ord(a[0]))
elif 2 < len(a) <= 10:
    if len(a) % 2 == 0:
        sr = len(a) // 2
    else:
        sr = len(a) // 2 +1
    print(int(ord(a[0])) + int(ord(a[sr])) + int(ord(a[-1])))
else :
    print(ord(a[-1]))

a=input()
if len(a)<=2 :
    print(ord(a[0]))
elif 2<len(a)<10 :
    if len(a)%2==0 :
        print(ord(a[0])+ord(a[-1])+ord(a[int(len(a)/2)-1]))
    else :
        print(ord(a[0])+ord(a[-1])+ord(a[int(len(a)/2)-1]))

else :
    print(int(ord(a[-1])))
#print(ord(a[0]))

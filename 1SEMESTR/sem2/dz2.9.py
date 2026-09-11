'''f=open('input.txt')
a=f.readlines()'''
a=input()
a=a.replace(' ','')
a=a.replace('...',' ')
a=a.replace('.',' ')
a=a.replace('!',' ')
a=a.replace('?',' ')
print(a.count(' '))

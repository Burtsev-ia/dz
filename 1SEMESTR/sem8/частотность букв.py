
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
uppers = ''.join([i.upper() for i in alphabet])
##print (alphabet + uppers)
d = dict.fromkeys([i for i in alphabet], 0)
def counts_in_dict(t) :
    for i in range(len(t)) :
        if t[i] in uppers :
            t = t.replace(t[i],t[i].lower(),1)
    for i in t :
        if i in alphabet :
            d[i] += 1

line = input()
while 1 > 0 :
    counts_in_dict(line)
    line = input()
    print(sorted(d.items(), key = lambda item : item[1], reverse = True))
    print('\n\n\n')
    




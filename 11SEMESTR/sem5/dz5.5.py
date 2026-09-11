

def th(t,a) :

    s=['a','abbr','b','body','caption','cite','code','div','form','h1','h2','h3','h4','h5','h6','header','i','s']
    if t in s :
        return (f"<{t}>{a}</{t}>")
    else :
        return('введен неверный тег')


t=input()
a=input()
print(th(t,a))

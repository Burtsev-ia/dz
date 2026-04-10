tags = ['a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's']
t = input()
if t not in tags:
    print('Введён неверный тег')
else:
    a = input()
    print(f'<{t}>{a}</{t}>')

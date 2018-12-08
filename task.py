
a=input('enter sentence:')

file='file.txt'
print('file saved')
choice=input('do u want to read(y/n)')
print(choice)
if choice=='y':
        f = open(file, 'r', encoding='utf-8')
        print(f.read())
else:
        print('it will not be read')

choice1=input('dou want to edit(y/n)')
print(choice1)
if choice=='y':
    b=input('enter old word')
    c=input('enter new word')
    f = open(file, 'r')
    filedata = f.read()
    newdata = file.replace(b, a)

    f = open(file, 'w')
    f.write(newdata)
    f.close()
    print(f.read())

### writing in file

file='file.txt'
try:
    with open(file,'w',encoding='utf-8') as k:
        k.write('i am vimarsh shah\n')
        k.write('i love cricket and football\n')

except Exception as e:
    print(e)


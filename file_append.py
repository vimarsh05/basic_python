## appending a file

file='file.txt'
try:
    with open(file,'a',encoding='utf-8') as k:
        k.write('i am vimarsh bhavin shah\n')
        k.write('i love cricket and football and kabbadi\n')

except Exception as e:
    print(e)

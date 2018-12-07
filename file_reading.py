## reading a file

global file
file='file.txt'## first make a file
try:
    f=open(file,'r',encoding='utf-8')
    print(f.read())

except Exception as e:
    print(e)




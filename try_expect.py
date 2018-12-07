a=int(input('enter value of a:'))
b=int(input('enter value of b:'))
try:
    c=a+b
    d=a-b
    e=a/0
    print(c,d,e)

except Exception as e:
    print(e)

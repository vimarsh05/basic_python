num=int(input('enter positive number:'))

result=0
while num>0:
    digit=num%10
    result=result+digit
    num=num//10


print('sum is',result)



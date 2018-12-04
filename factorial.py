a=int(input('enter value of a:'))
factorial=1

if (a<0):
    print('factorial is not possible')

if (a==0):
    print('factorial of 0 is 1')

if (a>0):
    for i in range(1,a+1):
         factorial=factorial*i
    print('the factorial of ',a,'is',factorial)
a=int(input('enter value of a:'))
b=int(input('enter value of b:'))
c=int(input('enter value of c:'))

##maxima

if a>b:
    if a>c:
        print('a has maximum value')

if b>c:
    if b>a:
        print('b has maximum value')


else:
    print('c has mamximum value')


##minima


if a<b:
    if a<c:
        print('a has minimum value')



if b<c:
    if b<a:
        print('b has minimum value')


else:
    print('c has minimum value')


##middle number

if a>b:
    if a<c:
        print('a is middle number')
    if a>c:
        print('c is middle number')

else:
    print('b is middle number')


##equal or not

if a==b>c:
    print('a and b is equal and minimum and c has minimum value')

if a==b<c:
    print('a and b is equal and maximum and c has maximum value')

if b==c>a:
    print('b and c is equal and maximum and a has minimum value')

if b==c<a:
    print('b and c is equal and minimum and a has maximum value')

if c==a>b:
    print('c and a is equal and maximum and b has minimum value')

if c==a<b:
    print('c and a is equal and minimum and b has maximum value')
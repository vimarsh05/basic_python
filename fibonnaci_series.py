n=int(input('enter numbers in series:'))

first=0
second=1
for i in range(n):
    print(first)
    temp=first
    first=second
    second=second+temp


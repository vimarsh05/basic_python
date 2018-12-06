n=int(input('enter value of rows:'))


##for same numbers in row
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(row,end='')
    print()


##for different numbers in rows
#
# for row in range(n,0,-1):
#     for col in range(1,row+1):
#         print(col,end='')
#     print()
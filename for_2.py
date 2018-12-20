for row in range(9):
    for col in range(4):
        if row==0 or (col==3 and (row==1 or row==2 or row==3)) or row==4 or (col==0 and(row==5 or row==6 or row==7)) or row==8:
            print('*',end=' ')

        else:
            print(end='  ')
    print()
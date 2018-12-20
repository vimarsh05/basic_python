for row in range(7):
    for col in range(4):
        if (col==0 and (row==0 or row==1 or row==2)) or row==3 or (col==3 and (row==4 or row==5 or row==6)) :
            print('*',end=' ')

        else:
            print(end='  ')
    print()
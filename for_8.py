for row in range(5):
    for col in range(4):
        if col==0 or col==3 or  (row==0 and (col==1 or col==2)) or (row==2 and (col==1 or col==2)) or (row==4 and (col==1 or col==2)):
            print('*',end=' ')

        else:
            print(end='  ')

    print()
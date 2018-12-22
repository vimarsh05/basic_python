for row in range(5):
    for col in range(5):
        if col==4 or row==0 or (col==0 and (row==1 or row==2)) or  (row==2 and (col==1 or col==2 or col==3)):

            print('*',end=' ')

        else:
            print(end='  ')

    print()
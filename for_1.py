for row in range(5):
    for col in range(5):
        if col==2 or row==4 or (col==0 and row==2) or (col==1 and row==1):
            print('*',end=' ')

        else:
            print(end='  ')
    print()
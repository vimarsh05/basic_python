for row in range(7):
    for col in range(4):
        if row==0 or row==3 or row==6 or (col==0 and (row==1 or row==2)) or ((col==0 or col==3) and (row==4 or row==5)):
            print('*',end=' ')

        else:
            print(end='  ')

    print()
for row in range(7):
    for col in range(6):
        if col==0 or (col==4 and (row!=1 and row!=2)) or (row==0 and (col>0 and col<4)) or (row==6 and (col>0 and col<4)) or (row==3 and (col>2 and col<6)):
            print('*',end='')
        else:
            print(end=' ')
    print()
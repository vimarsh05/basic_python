list1=[23,0,34,6,6,0]
print('unsorted lidt1',list1)

for i in range(len(list1)):
    min_val=min(list1[i:])
    min_ind=list1.index(min_val,i)
    if list1[i] !=list1.index(min_val,i):
       list1[i],list1[min_ind]=list1[min_ind],list1[i]

    print('sorted list',list1)
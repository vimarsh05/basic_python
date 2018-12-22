list1=['abc','123']
for i in list1: ## output will not be seen as for loop is infinite loop as first value is abc and second value is 123
    list1.append(i)
print(list1)
movies=['the holy grail','terry jones',['graham chapman'['john cleese','eric idle']]]
for each_items in movies:
    if isinstance(each_items,list):
        for nested_item in each_items:
            print(nested_item)

    else:
        print(each_items)
def change(list):
    list_new = ''
    for i in range(len(list)):
        if i == len(list) - 1:
            list_new += 'and ' + list[i]
        else:
            list_new += list[i] + ','
    return list_new


spam = ['apple', 'banana', 'tofu', 'cats']
print(change(spam))
 

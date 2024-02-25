list1=[1,2,3,4]
list2=[1,1,3,4]
list3=[]
for i in list1:
    if i in list1 and i in list2:
        list3.append(i)
print(list3)        
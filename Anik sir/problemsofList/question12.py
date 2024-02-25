list1=[1,2,3,4,12,34]
list2=[1,1,3,4]
union_list=[]
for i in list1:
    if i in list1+list2:
         union_list.append(i)     
print(union_list)        
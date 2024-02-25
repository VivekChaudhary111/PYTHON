n=int(input("Enter the total number of items:"))
List=[]
for i in range(1,n+1):
     list_items=int(input(f"Enter the List item {i}:"))
     List.append(list_items)
print(List)

m=int(input("Number of items to be removed from the list:"))
elements_remove_list=[]
for i in range(1,m+1):
     list_items=int(input(f"Enter the List item {i}:"))
     elements_remove_list.append(list_items)  
item=0
new_list=[]     
for i in List:
     if i in elements_remove_list:
          continue
     else:
          new_list.append(i)
print(new_list)          
        
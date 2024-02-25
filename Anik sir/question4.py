n=int(input("Enter the total number of items:"))
List=[]
for i in range(1,n+1):
     list_items=int(input(f"Enter the List item {i}:"))
     List.append(list_items)
print(List)


reverse_list=[]
for i in range(n):
     a=List.pop()
     reverse_list.append(a)
print(reverse_list)     

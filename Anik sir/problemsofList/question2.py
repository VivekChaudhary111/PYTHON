n=int(input("Enter the total number of items:"))
List=[]
for i in range(1,n+1):
     list_items=int(input(f"Enter the List item {i}:"))
     List.append(list_items)
print(List)
max_item=0
for i in List:
     if i>max_item:
          max_item=i
print(max_item)          
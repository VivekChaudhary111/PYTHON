n=int(input("Enter the total number of items:"))
List=[]
for i in range(1,n+1):
     list_items=int(input(f"Enter the List item {i}:"))
     List.append(list_items)
print(List)
sum=0
for i in range(n):
     sum+=List[i]
print(f"THe sum of of the list items is {sum}")     
     


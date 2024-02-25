#n=int(input("Enter the total number of items:"))
#List=[]
#for i in range(1,n+1):
#     list_items=int(input(f"Enter the List item {i}:"))
#     List.append(list_items)
#print(List)     

num=int(input("Enter the number of elements to add to the list:"))
List=[0]*num
print("Original List:",List)
for i in range(num):
    element=int(input(f"Enter element {i+1}:"))
    List[i]=element

print(f"finally the List is {List}")    
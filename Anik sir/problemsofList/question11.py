n=int(input("Enter the total number of items:"))
List=[]
for i in range(1,n+1):
     list_items=int(input(f"Enter the List item {i}:"))
     List.append(list_items)
print(List)

count_even=0
count_odd=0
for i in List:
     if i%2==0:
          count_even+=1
     else:
          count_odd+=1
print(f"The number of even numbers in List is {count_even} \nThe number of odd numbers in List is {count_odd}")         
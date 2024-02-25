n=int(input("Enter the total number of items:"))
List=[]
for i in range(1,n+1):
     list_items=int(input(f"Enter the List item {i}:"))
     List.append(list_items)
print(List)
occurence=int(input("Enter the element for which no. of occurrence to be find:"))
count=0
for i in List:
    if i==occurence:
       count+=1
              
print(f"No.of occurrence of {occurence} are {count}")           
          
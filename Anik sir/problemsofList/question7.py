n=int(input("Enter the total number of items:"))
List=[]
for i in range(1,n+1):
     list_items=int(input(f"Enter the List item {i}:"))
     List.append(list_items)
print(List)
'''
finalList=[]
count=0
for i in List:
     for j in List:
          if i==j:
               count+=1
               continue
          else:
               if count==1:
                finalList.append(i)
print(finalList)
'''
finalList = []
for i in List:
     if i not in finalList:
          finalList.append(i)
print(finalList)          
     
myDict={}
n=int(input("Enter the number of items to add:"))
for i in range(1,n+1):
      x,y=(input(f"Enter space separated Name and age pairs {i}:").split())
      myDict.update({x:int(y)})
      
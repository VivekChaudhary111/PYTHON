'''myDict={}
n=int(input("Enter the number of items to add:"))
for i in range(1,n+1):
      x,y=(input(f"Enter space separated item and price pairs {i}:").split())
      myDict.update({x:int(y)})
print(myDict)
sum=0
for i in myDict.values():
      sum+=i
print(sum) '''     

# Problem Statement:
# You are required to create a Python program that allows a user to input key value pairs to construct a
#dictionary. The program should follow these steps:
# 1. Prompt the user to enter the number of key-value pairs they want to add.
# 2. For each pair, prompt the user to enter a key and its corresponding value.
# 3. Construct a dictionary with the provided key-value pairs.
# 4. Print out the resulting dictionary.

n = int(input("Enter the number of key-value pairs they want to add: "))
dict={}
for i in range(n):
      x=input("Enter the key: ")
      y=input("Enter the value: ")
      dict.update({x:y})
print(dict)  

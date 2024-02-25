# Assignment 2: Dictionary Operations
# Problem Statement:
# Given the dictionary inventory representing items in a store, perform the following operations:
# inventory = {
# "apple": 10,
# "banana": 5,
# "orange": 8,
# "grape": 3
# }
# 1. Add 2 more apples to the inventory.
# 2. Check if "banana" is in the inventory. Print a message accordingly.
# 3. Reduce the quantity of grapes by 1.
# 4. Print the total number of items in the inventory.

inventory = {
 "apple": 10,
 "banana": 5,
 "orange": 8,
 "grape": 3
 }
inventory["apple"]+=2

if "banana" in inventory:
    print("Banana is available")
inventory["grape"]-=1
print(inventory)
count=0
for i in inventory:
    count+=1
print(f"Number of items in inventory are {count}")    

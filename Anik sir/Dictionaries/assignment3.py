# Assignment 3: Dictionary Iteration and Manipulation
# Problem Statement:
# Given the dictionary fruits:
# fruits = {
# "apple": 2,
# "banana": 5,
# "orange": 3,
# "grape": 7
# }
# 1. Print the names of fruits with quantities greater than 4.
# 2. Double the quantity of oranges.
# 3. Create a new dictionary more_fruits with the following items: {"kiwi": 4,"pear": 6}.
# 4. Add the items from more_fruits to fruits.
# 5. Print the updated fruits dictionary.

fruits = {
 "apple": 2,
 "banana": 5,
 "orange": 3,
 "grape": 7
 }
for x,y in fruits.items():
    if y>4:
        print(x,":",y)
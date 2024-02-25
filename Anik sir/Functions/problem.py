# Problem Statement:
# Write a function that takes a list of numbers
# as an argument and returns a sum of the squares of those numbers

def sum_of_squares(x):
    sum_of_squares = 0
    for i  in  x:
        sum_of_squares += i**2
    print("sum of squares", sum_of_squares)    
numbers = [2,3,4,5,6,7,8,9]    
sum_of_squares(numbers)
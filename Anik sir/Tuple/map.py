'''
user_input=input("Enter the numbers separated by spaces:")
x=map(int, user_input.split())
print(x) 

numbers =list(map(int, user_input.split())) 

squared_numbers=list(map(lambda x:x**2, numbers))
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
'''
# TO check that numbers separated by spaces are even or odd numbers
user_input=input("Enter the numbers separated by spaces:")
numbers =list(map(int, user_input.split())) 
even_odd_checker =list(map(lambda x:"Even" if x%2==0 else "Odd", numbers))
print("Results", even_odd_checker)

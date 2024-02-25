# A function in python can return data as a result.
# In python a function is defined using the keyword def .

# without parameter
def my_function():
    print("Hello from a function")

my_function() # To call a function 

print()

# with parameter
def my_function1(fname):
    print("My name is " +fname)

my_function1("Vivek")
my_function1("Rakshit")
my_function1("Kamal")    

def my_function2(fname,lname):
    print(fname +" "+ lname)

my_function2("Vivek","Chaudhary")   

def my_function3(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function3(fruits)


def my_function4(x):
    return 5*x

print(my_function4(3))
print(my_function4(4))
print(my_function4(5))
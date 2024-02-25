# Immutable Data types
def modify_string(s):
    s+= " World!"
    print("Inside the function modify_string:",s)

greeting = "Hello"
modify_string(greeting)
print("Outside the function modify_string:",greeting)    

def modify_tuple(t):
    # Tuples are immutable, so creating a new tuple
    t += (4,5)
    print("Inside the function modify_tuple:",t)
coordinates =(1,2,3)
modify_tuple(coordinates)
print("Inside the function modify_tuple:",coordinates) 

# Mutable Data Types
def modify_list(lst):
    lst.append(4)
    lst[0] = 99
    print("Inside the function modify_list:",lst)
numbers = [1,2,3]
modify_list(numbers)
print("Inside the function modify_list:",numbers)

def modify_dict(d):
    d['new_key'] = 'new_value'
    print("Inside the function modify_dict:",d)

my_dict = {'key1': 'value1','key2': 'value2'}
modify_dict(my_dict)
print("Inside the function modify_dict:",my_dict)

def modify_set(s):
    s.add(4)
    print("Inside the function modify_set:",s)
my_set = {1,2,3}
modify_set(my_set)
print("Inside the function modify_set:",my_set)

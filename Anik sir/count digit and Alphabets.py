
username="GLA202307060159"
alphas=0
digits=0
for i in range(len(username)):
    if username[i].isalpha():
        alphas+=1

    elif username[i].isdigit():
        digits+=1  

print(f"Number of alphabets:{alphas}")   
print(f"Number of digits:{digits}")     

#counting Number of Alphabets,digits,spaces, and special characters        
password="Anik@#$1234  5"
alphas=0
digits=0
special=0
spaces=0
for i in range(len(password)):
    if password[i].isalpha():
        alphas+=1

    elif password[i].isdigit():
        digits+=1 

    elif password[i].isspace():
        spaces+=1  

    else:
        special+=1  

print(f"Number of alphabets:{alphas}")   
print(f"Number of digits:{digits}")
print(f"Number of spaces:{spaces}")     
print(f"Number of special characters:{special}")

#print alphabets and digits in Something
username1=input("Enter mixed character of digits and numbers:")
alphas=""
digits=""
for i in range(len(username1)):
    if username1[i].isalpha():
        alphas+=username1[i]

    elif username1[i].isdigit():
        digits+=username1[i] 

print(f"Alphabets are:{alphas}")   
print(f"Digits are:{digits}")

#logic 2:
username2=input("Enter mixed character of digits and numbers:")
alphas=""
digits=""
for i in username2:
    if i.isalpha():
        alphas+=i

    elif i.isdigit():
        digits+=i 

print(f"Alphabets are:{alphas}")   
print(f"Digits are:{digits}")




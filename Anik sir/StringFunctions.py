text1="Python Programming"
text2="My University name is : GLA University"

#remove leading and trailng whitespaces
trimmed_text=text1.strip()
print(trimmed_text)

#convert to uppercase and lowercase
upper_case=text1.upper()
lower_case=text1.lower()
print("Uppercase:",upper_case)
print("Lowercase:",lower_case)

#replace text
text1=text1.replace("Programming","Coding")
print(text1)

#find_function
index=text2.find("GLA")
print(index)

#Capitalise_function
text="hello world"
capitalized_text=text.capitalize()
print(capitalized_text)

#title function
title_text=text.title()
print(title_text)

#isalpha() function and isdigit()
text="abc"
print(text.isalpha())

text="abc123"
print(text.isalpha())

number="123"
print(number.isdigit())

number="abc123"
print(number.isdigit())

#reverse a string
user_input=input("Enter th data:")
reverse=user_input[::-1]
print(reverse)







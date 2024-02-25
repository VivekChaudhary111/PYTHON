n1=int(input("Enter the start number:"))
n2=int(input("Enter the end number:"))

for i in range(n1, n2+1):
    if i % 2==0 and i % 3==0:
        print(f"{i}: Good Student!") 
    elif i % 2==0:
        print(f"{i}: Good")   
    elif i % 3==0:
        print(f"{i}: Student")
    else:
        print(i)    
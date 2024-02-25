
# Online_Shopping_Management_System

print("1. Add Product")
print("2. Display Product Catalog")
print("3. Update Product Quantity")
print("4. Search Product by ID")
print("5. Calculate Total Cost")
print("6. Remove Product by ID")
print("7. Exit")

Data=[]
Total_Cost=0

while True:
    n=int(input("Enter your choice:"))

    if n==1:
            p_id=input("Enter Product ID:")
            p_name=input("Enter Product Name:")
            quantity=int(input("Enter Quantity:"))
            price=float(input("Enter Price:"))
            Data.append([p_id,p_name,quantity,price])

    if n==2:
            print("Product Catalog:")
            for i in range(len(Data)):
                for j in range(1):
                    print(f"Product ID: {Data[i][0]}")
                    print(f"Product Name:{Data[i][1]}")
                    print(f"Quantity: {Data[i][2]}")
                    print(f"Price: ${Data[i][3]}")
                    print()

    if n==4:
            p=input("Enter the Product ID: ")
            q=int(input("Enter the new Quantity: "))
            for i in range(len(Data)):
                if p==Data[i][1]:
                    Data[i][2]=q
                    print("Quantity updated successfully")
                else:
                    continue
                  
    if n==5:
            for i in range(len(Data)):
                for j in range(1):
                    Total_Cost+=Data[i][2]*Data[i][3]
            print("Total Cost : ", Total_Cost)  

    if n==6:
            p=input("Enter the Product ID: ")
            for i in range(len(Data)):
                if p==Data[i][1]:
                    Data.remove([i])
                    print("Product ID Removed successfully")
                else:
                    continue

    if n==7:
            print("Thank you!")
            break
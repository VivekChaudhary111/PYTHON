
# Bridge_Toll_Management_System

print("1. Add Vehicle Entry")
print("2. Display Vehicle Entries")
print("3. Calculate Total Toll Collection")
print("4. Search Vehicle by Number")
print("5. Exit")
Data=[]
Total_Toll_Collection=0
while True:
    n=int(input("Enter your choice:"))
    if n==1:
            Vn=input("Enter Vehicle Number:")
            type=input("Enter Vehicle Type (Car/Truck/Bus):")
            toll=float(input("Enter Toll Amount:"))
            Data.append([Vn,type,toll])
    if n==2:
            print("Vehicle Entries:")
            for i in range(len(Data)):
                for j in range(1):
                    print(f"Vehicle Number:{Data[i][0]}")
                    print(f"Vehicle Type:{Data[i][1]}")
                    print(f"Toll Amount: ${Data[i][2]}")
                    print()
    if n==3:
            for i in range(len(Data)):
                for j in range(1):
                    Total_Toll_Collection+=Data[i][3]
            print("Total Toll Collection :",Total_Toll_Collection)
    if n==4:
            vn2=input("Enter the Vehicle number: ")
            for i in range(len(Data)):
                if vn2==Data[i][1]:
                    print(Data[i])
                else:
                    continue
    if n==5:
            print("Thank you!")
            break
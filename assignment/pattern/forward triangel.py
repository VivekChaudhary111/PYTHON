rows=int(input("Enter the no.of rows:"))

print('\nBackward Triangle:')
for i in range (1,rows+1):
    for j in range(rows-i+1):
        print("*",end=" ")
    print()
print('\nForward Triangle:')      
for i in range (1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()   
  
print('\nForward Triangle with the diffrence of 2:')      
for i in range (1,rows+1,2):
    for j in range(i):
        print("*",end=" ")
    print()  
print('\nBackward Triangle with the diffrence of 2:')      
for i in range (rows+1,1,-2):
    for j in range(i):
        print("*",end=" ")
    print()    
print('\nForward Triangle with the line with odd no. of * :')      
for i in range (1,rows+1):
    if i%2==0:
        pass
    else:
        for j in range(i):
             print("*",end=" ")
    print() 

n=int(input("number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()    
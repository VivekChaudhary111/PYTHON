rows=7
for i in range(1,rows+1):
    print((rows-i)*" ",end='')

    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i==4:
            print("*",end='')

        else:
            print(" ",end='')
    print()             
string=input()
count=0
for i in string:
    for j in string:
        if j==i:
            count+=1
    else:
        if count==1:
            print(i)
            break
    count=0    
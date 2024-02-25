n1=int(input())
n2=int(input())
lst=[]
if n1>1:
    for i in range(n1,n2+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            lst.append(i)
print(lst)


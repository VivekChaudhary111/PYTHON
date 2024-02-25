x=input()
N=int(x[0])
M=int(x[4])
List=[]
count=0
for i in range(N):
    for j in range(M):
        if (i+j)%2!=0:
            count+=1
            List.append((i,j))
print(List)
print(count)
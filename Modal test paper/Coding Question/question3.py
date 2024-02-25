n=list(map(int,input().split()))
out=[]
for i in n:
    if i%2!=0:
       out.append(i)  
if len(out)!=0:       
    for j in out:
        print(j**2,end=" ")  
else:
    print(None)    
       
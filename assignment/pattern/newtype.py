n=5
count=0
c1=0
a="1 "
print(a)
for i in range(n):
    
    for j in range(c1,len(a)):
        if a[j]==a[c1]:
            count+=1    
        else:
            print(count,a[c1],sep="",end="")
            
            x=str(count)+a[c1]
        
            
        
    print()
    c1=count
    count=0
    a=x       

   
    
      



       
               
            
                  


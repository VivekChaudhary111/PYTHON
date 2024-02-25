x=input()
Dictionary=eval(x)
a=[]
b=[]
c=[]
for i in Dictionary:
    if Dictionary[i]>40 or Dictionary[i]<20:
        a.append(i)
    else:
        b.append(i)
a.sort() 
b.sort()     
c.append(a)
c.append(b)
print(c)
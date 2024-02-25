def Prime(n):
    count=0
    for i in range(1, int((n/2)+1)):
        if n%i==0:
           count+=1
        else:
            continue 
    if count==1:
        print(f"{n} is prime number")  
    else:
        print(f"{n} is not prime number")  

Prime(87)
Prime(7)
Prime(19)            
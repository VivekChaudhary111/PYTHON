def sumOfNatural(n1, n2):
    sum=0
    for i in range(n1, n2+1):
        sum +=i
    print(f"Sum of natural numbers from {n1} to {n2} is {sum}") 

sumOfNatural(1, 100)      

num = int(input("Enter a number: "))

res = num % 2
out = 'ODD' * res + 'EVEN' * (1 - res)
print(out)
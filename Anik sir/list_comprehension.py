squares=[x**2 for x in range(1,11)]
print(squares)

even_numbers=[x for x in range(11) if x%2==0]
print(even_numbers)

results=["pass" if score>=60 else "Fail" for score in [56,75,49,84,67]]
print(results)

names=["Kamal","Vivek","Apransh","Rakshit"]
name_lengths=[len(name) for name in names]
print(name_lengths)

num=[x+2 for x in range(100) if x%5==0]
print(num)

# mytuple=("stud1", "stud2", "stud3")
# print(mytuple)
# print(len(mytuple))
# print(type(mytuple))

# tuple1=(1,2,3,4,5,6,7,8,9,10)
# tuple2=("hi","hello")
# print(tuple1,tuple2)
# tuple1=(1,2,3,4,5)
# tuple2=("a","b","c")
# tuple3= tuple1 + tuple2
# print(tuple3)

# tuple4=("stud1","stud2")
# print(tuple4*2)

#s=("s1","s2","s3","s4")
# for x in s:
#     print(x)
# for y in range(len(s)):
#     print(s[y])
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1        

# Tuple Slicing

s=("s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s5","s4","s5")
print(s[2])
print(s[2:5])
print(s[:6]) 
print(s[2:])
print(s[-4:])   

#function that returns integer values
print(s.count("s5"))
print(s.index("s5"))

s=("E1","E2","E3","E4","E5")
y=list(s)
y[1]="E6"
z=tuple(y)
print(z)

b=list(s)
b.append("E5")
t=tuple(b)
print(t)


#Upacking of tuples
students=("s1","s2","s3","s4")
(one, two, three, four)=students
print(one)
print(two)
print(three)
print(four)

students=("s1","s2","s3","s4")
(one, *two)=students  # "*" will always return a list
print(one)
print(two)

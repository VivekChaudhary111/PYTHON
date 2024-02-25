mylist1=["a","b","c"]
mylist1.remove("b")
print(mylist1)

mylist2=["a","b","c"]
mylist2.pop(0)
print(mylist2)

mylist3=["a","b","c"]
mylist3.pop()
print(mylist3)

mylist4=["a","b","c"]
del mylist4[0]
print(mylist4)

#mylist5=["a","b","c"]
#del mylist5
#print(mylist5) #return Error due to list does not exist that is not defined

mylist5=["a","b","c"]
mylist5.clear()
print(mylist5)

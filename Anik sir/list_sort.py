myData1=["orange","mango","kiwi","pineapple","banana"]
myData1.sort()
print(myData1)

myData2=[8,35,75,83,45,38]
myData2.sort()
print(myData2)

myData3=[8,35,75,83,45,38]
myData3.sort(reverse=True)
print(myData3)

myData4=[8,35,75,83,45,38]
myData4.reverse()
print(myData4)
for i in myData4:
    if i>myData4[0]:
        print(i)
        break
    else:
        continue    
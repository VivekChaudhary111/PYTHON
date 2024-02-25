
mylist1=["GLA","Sharda","LPU","Amity","Delhi University","Galgotias","CU"]
print(mylist1[1])
print(mylist1[-1])
print(mylist1[2:5])
print(mylist1[:4])
print(mylist1[2:])

if "GLA" in mylist1:
    print("Yes")

#append add an list item at the end
mylist2=[9,10,11]
mylist2.append(12)
print(mylist2)

#extent add an list at the end
List1=["a","b","c"]
List2=["m","p","y"]
List1.extend(List2)
print(List1)

myData = ["Milk","Tea","Coffee","Sugar","Bread"]
print(myData)

myData[1]="Black Tea"
print(myData)

myData[1:3]=["Black Tea","Cold coffee"]
print(myData)

myData[1:2]=["D1","D2"]
print(myData)

myData[1:3]=["myNewData"]
print(myData)

#insert new data item at an index
myData.insert(3,"Soft Drink")
print(myData)

list1=["a","b","c"]
list2=[1,2,3]

list3=list1 + list2
print(list3)

list1=["a","b","c"]
list2=[1,2,3]

for x in list2:
    list1.append(x)
print(list1)

newList=["apple","banana","cherry"]
finalList=newList.copy()
print(finalList)

newList=["apple","banana","cherry"]
finalList=list(newList)
print(finalList)

myData=["a","b","c"]
for x in myData:
    print(x)

myData1=["a","b","c"]
for i in range(len(myData1)):
    print(myData1[i])

myData2=["a","b","c"]
i=0
while i <len(myData2):
    print(myData2[i])
    i=i+1

myData3=["d","e","f"]
[print(x) for i in myData3]


veg=["Cabbage","potato","brinjal","tomato"]
newlist=[]

for x in veg:
    if "o" in  x:
        newlist.append(x)

    print(newlist)

veg=["Cabbage","potato","brinjal","tomato"]
newlist1=[x for i in veg if "o" in x]
print(newlist1)
    


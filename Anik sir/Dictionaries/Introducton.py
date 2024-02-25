# #Dictionaries are used to store data values in key:value pairs.
# MyDict={
#     "university": "GLA University",
#     "location": "Mathura",
#     "year": "2010"
# }

# print(MyDict)
# print(MyDict["year"])
# print(len(MyDict))
# print(type(MyDict))

# thisdict=dict(name="Vivek",age="18",country="Norway")
# print(thisdict)

# car={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }

# x=car.keys()
# print(x)

# car["color"]="White"
# print(car)
# print(x)

# thisdict={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# x=thisdict.items()
# print(thisdict)
# print(x)

# thisdict={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# if "model"in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary")

# if "Mustang" in thisdict.values():
#     print("Yes, 'Mustang' is one of the keys in the thisdict dictionary")

# MyDetails={
#     "university": "GLA University",
#       "location": "Mathura",
#           "year": "2010"
# }

# MyDetails["year"]=2018
# print(MyDetails)

# thisdict={
#     "university": "GLA University",
#       "location": "Mathura",
#           "year": "2010"
# }

# thisdict.update({"year":2020})
# print(thisdict)

# thisdict.pop("location") #pop() expected at least 1 argument
# print(thisdict)
# thisdict.popitem() #popitem() takes no arguments 
# print(thisdict)

thisdict={
    "university": "GLA University",
      "location": "Mathura",
          "year": "2010"
}

del thisdict["location"]
print(thisdict)

thisdict={
    "university": "GLA University",
      "location": "Mathura",
          "year": "2010"
}

# del thisdict 
# print(thisdict) # This line will give an error because this dictionary does not exist

thisdict={
    "university": "GLA University",
      "location": "Mathura",
          "year": "2010"
}

thisdict.clear()
print(thisdict)

print("The End!")
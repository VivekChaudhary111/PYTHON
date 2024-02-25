MyDict={
    "John":85,
    "Jane":90,
    "Bob":75,
    "Alice":95
}
MyDict.update({"Sam":80})
MyDict["Bob"]=80
print(MyDict)
MyDict.pop("Jane")
print(MyDict)
for name,scores in MyDict.items():
    print(f"{name}:{scores}")
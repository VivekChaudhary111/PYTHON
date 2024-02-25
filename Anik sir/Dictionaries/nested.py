myStudents ={
    "stud1":{
        "name":"Vivek",
        "year":2004
    },
    "stud2":{
        "name":"Rakshit",
        "year":2007
    },
    "stud3":{
        "name":"Kamal",
        "year":2011
    }
}
print(myStudents)

for x in myStudents:
    print(x)
print(myStudents["stud2"]["name"])   

for x,y in myStudents.items(): 
    print(x,y)
    
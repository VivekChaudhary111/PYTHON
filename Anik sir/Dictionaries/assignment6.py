student_names = ["Vivek", "Rakshit","Kamal"]
scores_in_test = [94,90,94]
myDict={}
for i in range (len(scores_in_test)):
    myDict.update({student_names[i]: scores_in_test[i]})    
print(myDict)
total_score=0
for i in myDict.values():
    total_score+=i
average_score=total_score/len(myDict)    
print(average_score)
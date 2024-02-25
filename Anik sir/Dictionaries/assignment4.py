Students={
    "Vivek":96,
    "kamal":97,
    "Rakshit":95
}
x=Students.values()

highest_grade=0
for i in x:
   if i>highest_grade:
      highest_grade=i
top_students=[student for student,i in Students.items() if student==highest_grade]   
print(f"The highest grade is: {highest_grade}")   
print(f"The student(s) with highest grade: {', '.join(top_students)}")
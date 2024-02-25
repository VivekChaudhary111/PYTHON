# taking multiple inputs at a time separated by comma
#x = [int(x) for x in input("Enter multiple value: ").split(",")]
#print("Number of list is: ", x)

# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
a=int(input())
x=input()
list=[]
if a==(len(x)/2)+1:
   for i in range(0,len(x),2):
       list.append(int(x[i]))
maxi=max(list)   
mini=min(list)                
m_diff=maxi-mini 
print(m_diff)
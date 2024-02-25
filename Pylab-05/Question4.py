colours=eval(input())
for i in colours:
    for j in colours:
        if i!=j:
            if (i=="R" and j=="G") or (i=="G" and j=="R"):
                colours.remove(i)
                colours.remove(j)
                colours.append("B")
            elif (i=="R" and j=="B") or (i=="B" and j=="R"):
                colours.remove(i)
                colours.remove(j)
                colours.append("G")
            elif (i=="G" and j=="B") or (i=="B" and j=="G"):
                colours.remove(i)
                colours.remove(j)
                colours.append("R")
        else:
            break    
    else:
        continue  
print(colours[0])        
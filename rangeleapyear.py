def rangeleapyear(start,end):
    for x in range(start,end+1):
        if (x%4==0) and (x%400==0 or x%100!=100):
            print(x,"\n")
#Test Case
rangeleapyear(1990,2020)
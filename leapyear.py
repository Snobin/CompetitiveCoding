def leapyear(n):
    if(n%4==0)and(n%400==0 or n%100!=0):
        return "Leap Year"
    else:
        return "not Leap Year"
    
#Test Case
n=2024
print(leapyear(n))
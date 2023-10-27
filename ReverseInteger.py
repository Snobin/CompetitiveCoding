def reverse(x):
    
    min=-2**31
    max=2**31 - 1
    if x>max or x<min:
         return 0
    elif x>0:
        answer=int(str(x)[::-1])
    else:
        answer=-int(str(-x)[::-1])
    
    if answer>max or x<min:
        return 0
    return answer

#Test Case

x = -123
y=120
print(reverse(x))
print(reverse(y))
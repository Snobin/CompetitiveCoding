def isSameAfterReversals(num):
    temp=int(str(num)[::-1])
    if(len(str(num))==len(str(temp))):
        return True
    else:
        return False
    
#Test Case

x=1800
y=123

output1=isSameAfterReversals(x)
output2=isSameAfterReversals(y)
print(output1)
print(output2)
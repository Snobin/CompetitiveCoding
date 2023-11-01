def addBinary( a, b):
    inta=int(a,2)
    intb=int(b,2)
    sum=inta+intb
    answer=bin(sum)[2:]
    return answer


#Test Case
a = "1010"
b = "1011"
print(addBinary(a,b))
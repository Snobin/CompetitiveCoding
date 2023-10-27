def addToArrayForm(num, k):
    sums=0
    length=len(num)
    for i in range(length):
        sums+=num[i]*10 ** (length-i-1)
        
    answer=sums+k
    
    return [int(element) for element in str(answer)]

#Test Case

num = [1,2,0,0]
k = 34
print(addToArrayForm(num,k))

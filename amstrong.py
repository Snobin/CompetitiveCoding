def amstromg(n):
    length=len(str(n))
    number=n
    sum=0
    for i in range(length):
        temp=n%10
        sum+=temp**length
        n=n//10
    if sum==number:
        return True
    else:
        return False
    
#Test Case

n=9474
print(amstromg(n))
def prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return "no prime"
        
    return "prime"
#Test Case

n=6
print(prime(n))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#Test Case

a=10
b=20
print(gcd(a,b))
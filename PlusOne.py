def plusOne(digits):
    sums=0
    length=len(digits)
    for i in range(length):
        sums+=digits[i]*10 ** (length-i-1)
    answer=sums+1
    return [int(element) for element in str(answer)]
x=[1,2,9]
print(plusOne(x))
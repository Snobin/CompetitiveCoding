def reverseBits(n):
    bin_rev=format(n,'032b')
    rev=str(bin_rev)[::-1]
    ans=int(rev,2)
    return ans

#Test Case

x="00000010100101000001111010011100"
print(reverseBits(x))
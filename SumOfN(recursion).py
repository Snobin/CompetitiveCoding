class Solution():
    def SumOfN(self,n):
        if n==1:
            return 1
        return n+self.SumOfN(n-1)

#Test Case
ans=Solution()
n=5
print(ans.SumOfN(n))
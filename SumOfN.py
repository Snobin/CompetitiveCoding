class Solution():
    def SumOfN(self,n):
        sum=0
        for i in range(n+1):
            sum=sum+i
        return sum
    
#Test Case
ans=Solution()
print(ans.SumOfN(5))
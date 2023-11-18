class Solution():
    def maxProfit(self,arr):
        n=len(arr)
        maxi=0
        minu=arr[0]
        for i in range(n):
            minu=min(minu,arr[i])
            maxi=max(maxi,arr[i]-minu)
        return maxi
    
#Test Case
ans=Solution()
arr=[7,1,5,3,6,4]
print(ans.maxProfit(arr))
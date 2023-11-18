class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxi=0
        n=len(prices)
        for i in range(n):
            for j in range(i+1,n):
                if(prices[j]>prices[i]):
                    maxi=max(prices[j]-prices[i],maxi)
        return maxi


ans=Solution()
#Test Case
prices = [7,1,5,3,6,4]
print(ans.maxProfit(prices))
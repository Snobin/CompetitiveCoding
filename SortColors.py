class Solution():
    def sortColors(self,nums):
        length=len(nums)
        cnt0=0
        cnt1=0
        cnt2=0
        for num in nums:
            if num==0:
                cnt0+=1
            elif num==1:
                cnt1+=1
            else:
                cnt2+=1
        for i in range(cnt0):
            nums[i]=0
        for i in range(cnt0,cnt0+cnt1):
            nums[i]=1
        for i in range(cnt1+cnt0,length):
            nums[i]=2
        return nums

ans=Solution()

#Test Case
nums=[1,2,1,2,0,0,1]
print(ans.sortColors(nums))
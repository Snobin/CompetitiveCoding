class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        c1=0
        c2=0
        c3=0
        for nnum in nums:
            if nnum==0:
                c1+=1
            elif nnum==1:
                c2+=1
            else:
                c3+=1
        for i in range(c1):
                nums[i]=0
     
        for i in range(c1,c1+c2):
                nums[i]=1

        for i in range(c1+c2,length):
                nums[i]=2
        return nums
    
    
ans=Solution()

#Test Case
nums=[1,2,1,2,0,1]
print(ans.sortColors(nums))
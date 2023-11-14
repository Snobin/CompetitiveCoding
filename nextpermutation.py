class Solution():
    def nextPermutation(self,nums):
        length=len(nums)
        print(length)
        ind=-1
        for i in range(length-2,-1,-1):
            if(nums[i]<nums[i+1]):
                ind=i
                break
        if ind==-1:
            return nums[::-1]
        for i in range(length-1,ind,-1):
            if(nums[i]>nums[ind]):
                break
        nums[i],nums[ind]=nums[ind],nums[i]
        nums[ind+1:]=reversed(nums[ind+1:])
        return nums
    
#Test Case
sol=Solution()
num=[1,2,3]
print(sol.nextPermutation(num))

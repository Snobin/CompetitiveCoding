def rotate(nums, k):
    k=k%len(nums)
    print(nums[-k:])
    nums=nums[-k:]+nums[:-k]
    print(nums)
#Test Case
nums=[1,2,3,4,5]
k=2
rotate(nums,k)
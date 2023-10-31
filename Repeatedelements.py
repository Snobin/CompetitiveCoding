def repeatedelemet(nums):
    
    for i in range(len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i]==nums[j]:
                print(nums[i])
    
nums=[1,2,3,4,2,5,4,1]
repeatedelemet(nums)
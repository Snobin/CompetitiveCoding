def findDuplicate(nums):
    checking=set()
    for n in nums:
        if n in checking:
            return n
        else:
            checking.add(n)
            
#Test Case

nums = [1,3,4,2,2]
print(findDuplicate(nums))
def singleNumber(nums):
    result=0
    for n in nums:
        result^=n
    return result

#Test Case
nums = [4,1,2,1,2]
print(singleNumber(nums))

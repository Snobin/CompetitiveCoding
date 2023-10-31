def removeElement(nums,val):
    length=len(nums)
    index=0
    for x in range(length):
        if nums[x]!=val:
            nums[index]=nums[x]
            index+=1
    return index

#Test Case

nums=[3,2,2,3]
val = 3
print(removeElement(nums,val))
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))
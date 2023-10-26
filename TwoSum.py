def twosum(nums,target):
    dict={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in dict:
            return [dict[complement],i]
        dict[num]=i
        
    return []

#Test case

nums = [5,10,15,20]
target = 35
output=twosum(nums,target)
print(output)
        
    
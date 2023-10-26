def majorityElement(nums):
    answer=None
    count=0
    for n in nums:
        if count==0:
            answer=n
            count+=1
        elif n==answer:
            count+=1
        else:
            count-=1
    return answer

#Test Case

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
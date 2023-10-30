def findErrorNums( nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sets=set()
        for num in nums:
            
            if num in sets:
                b=num
                break
            sets.add(num)

        leng=len(nums)
        tsum=leng*(leng+1)//2
        sums=sum(nums)
        c=tsum-sums+b
        c=[b,c]
        return c
    
#Test Case

nums=[1,2,2,4]
print(findErrorNums(nums))
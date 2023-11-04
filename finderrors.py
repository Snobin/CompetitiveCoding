
def findErrorNums( nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_count = {}
        duplicate = None
        for num in nums:
            if num in num_count:
                duplicate = num
            num_count[num] = num_count.get(num, 0) + 1

        for num in range(1, len(nums) + 1):
            if num not in num_count:
                missing = num

        return [duplicate, missing]


#Test case
nums=[1,2,3,4,5,1]
print(findErrorNums(nums))
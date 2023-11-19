
import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1 
    # print(maxi)
    sum=0
    for i in range(n):
        sum += arr[i]
        if sum > maxi:
            maxi = sum
        if maxi < 0:
            sum = 0
    return maxi


#Test Case
arr = [-2, -3, 4,2, 1, -5]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)

#Test Case
arr=[10,-1,-5,15]
n=len(arr)
print(maxSubarraySum(arr,n))
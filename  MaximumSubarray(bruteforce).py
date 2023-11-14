
import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1 

    for i in range(n):
        for j in range(i, n):
         
            summ = 0

     
            for k in range(i, j+1):
                summ += arr[k]

            maxi = max(maxi, summ)

    return maxi


arr = [-2, -3, 4, -1, 0,-2,2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)

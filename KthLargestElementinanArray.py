import heapq
def findKthLargest(arr, k):
    ans=[]
    for num in arr:
        heapq.heappush(ans,-num)
    k-=1
    while k>0:
        heapq.heappop(ans)
        k-=1
    return -ans[0]

#Test Case
nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums,k))

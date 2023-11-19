# ans=[1,2,4,5,6,7,9,8]
# k=1
# import heapq
# def findKthLargest( arr, k):
#         pq = []
#         n = len(arr)
#         for i in range(n):
#             heapq.heappush(pq, -arr[i])
#         f = k - 1
#         print(pq)
#         while f > 0:
#             heapq.heappop(pq)
#             f -= 1
#         print("Kth Largest element", pq[0])
#         return -pq[0]
# findKthLargest(ans,k)
n=5
rotated = [[0 for _ in range(n)] for _ in range(n)]
print(rotated)
ans=[1,2,3,4]
bcd=[5,6]
ans[:2]=bcd[:1]
print(ans)
class Solution():
    def BubbleSort(self,arr):
        for i in range(len(arr)):
            swapped=False
            for j in range(0,len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped=True
            if swapped==False:
                break
        return arr

ans=Solution()
arr=[1,3,2,5,4]
print(ans.BubbleSort(arr))
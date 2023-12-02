class Solution():
    def SelectionSort(self,arr):
        length=len(arr)
        for i in range(length):
            min_index=i
            for j in range(i+1,length):
                if arr[min_index]>arr[j]:
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr

ans=Solution()
arr=[1,4,6,2]
answer=ans.SelectionSort(arr)
print(answer)
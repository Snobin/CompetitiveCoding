class Solution():
    def InsertionSort(self,arr):
        length=len(arr)
        for i in range(1,length):
            key=arr[i]
            j=i-1
            while j>=0 and key < arr[j]:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=key
        return arr
    
#Test Case
arr=[1,2,3,4,6,5]
ans=Solution()
print(ans.InsertionSort(arr))
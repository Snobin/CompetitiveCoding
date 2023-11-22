class Solution():
    def merge(self,a,b):
        m=len(a)
        n=len(b)
        left=m-1
        right=0
        while left>=0 and right <n:
            if a[left]>b[right]:
                a[left],b[right]=b[right],a[left]
            else:
                break
        a.sort()
        b.sort()
        for i in range(m):
            print(a[i])
        for j in range(n):
            print(b[j])

ans=Solution()
#Test case
a=[1,2,4]
b=[1,3]
ans.merge(a,b)
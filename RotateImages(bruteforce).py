class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        rotated=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n-i-1]=matrix[i][j]

        return rotated
        
#Test Case
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
ans=Solution()
print(ans.rotate(matrix)) 
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        an = []
        for i in range(1, numRows + 1):
            an.append(self.pas(i))
        return an
    def pas(self, row):
        ans = 1
        ansRow = [1]
        for col in range(1, row ):
            ans *= (row - col )
            ans //= col
            ansRow.append(ans)
        return ansRow


#Test case

answer=Solution()
print(answer.generate(5))
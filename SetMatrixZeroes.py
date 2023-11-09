def setZeroes( matrix):
        rows,cols=len(matrix),len(matrix[0])
        row=[0]*rows
        col=[0]*cols
        for i in range (rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    col[j]=1
                    row[i]=1
        for i in range(rows):
            for j in range(cols):
                if row[i] or col[j]:
                    matrix[i][j]=0
        return matrix
    
#Test Case
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(setZeroes(matrix))
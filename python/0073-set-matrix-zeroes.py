class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        z_rows, z_columns = [], []
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    z_rows.append(i) # fill lists with zeroes indexes
                    z_columns.append(j) # 
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i in z_rows:
                    matrix[i][j] = 0
                if j in z_columns:
                    matrix[i][j] = 0
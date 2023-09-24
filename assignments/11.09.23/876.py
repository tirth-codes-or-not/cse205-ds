class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])

        new_matrix = []
        for i in range(column):
            current = []
            for j in range(row):
                current.append(matrix[j][i])
            new_matrix.append(current)
        return new_matrix
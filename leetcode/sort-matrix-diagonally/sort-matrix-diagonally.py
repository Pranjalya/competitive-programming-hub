class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        d = {i: [] for i in range(-n+1, m)}
        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])
        for i in d.keys():
            d[i].sort()
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop(0)
        return mat
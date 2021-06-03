class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Using DFS
        m, n, p = len(s1), len(s2), len(s3)

        if p != m + n:
            return False
        if m == 0:
            if s2 == s3:
                return True
            else:
                return False
        if n == 0:
            if s1 == s3:
                return True
            else:
                return False

        stack = [[0,0]]
        visited = [[False for i in range(n+1)] for j in range(m+1)]

        while len(stack) != 0:

            q = stack.pop()
            i, j = q[0], q[1]
            visited[i][j] = True

            if i == m and j == n: return True
            if i < m and (not visited[i+1][j]) and s1[i] == s3[i+j]:
                stack.append([i+1, j])
            if j < n and (not visited[i][j+1]) and s2[j] == s3[i+j]:
                stack.append([i, j+1])

        return False
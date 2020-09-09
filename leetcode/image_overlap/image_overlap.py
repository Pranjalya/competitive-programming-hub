from collections import Counter

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        A1, B1 = [], []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    A1.append((i,j))

        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j]:
                    B1.append((i,j))
                    
        values = []
        
        for xa, ya in A1:
            for xb, yb in B1:
                values.append((xa-xb, ya-yb))
                
        counter = Counter(values)

        return max(counter.values() or [0])
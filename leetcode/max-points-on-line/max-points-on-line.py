from itertools import combinations
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        slpcnt = defaultdict(set)
        for a, b in combinations(points, r=2):
            try:
                m = (b[1]-a[1])/(b[0]-a[0])
                c = a[1] - m*a[0]
            except:
                m = 'inf'
                c = a[0]
            slpcnt[(m,c)].add((a[0], a[1]))
            slpcnt[(m,c)].add((b[0], b[1]))
        return len(max(slpcnt.values(), key=len))

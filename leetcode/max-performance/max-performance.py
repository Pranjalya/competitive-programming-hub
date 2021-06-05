class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = sorted(zip(speed, efficiency), key=lambda x: x[1], reverse=True)
        heap, total, ans = [], 0, 0
        for s, e in eng:
            heappush(heap, s)
            if len(heap) <= k:
                total += s
            else:
                total += s - heappop(heap)
            ans = max(ans, total*e)
        return ans % (10**9+7)
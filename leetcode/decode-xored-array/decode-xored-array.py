class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [0]*(len(encoded)+1)
        ans[0] = first
        for i in range(1, len(encoded)+1):
            ans[i] = ans[i-1] ^ encoded[i-1]
        return ans


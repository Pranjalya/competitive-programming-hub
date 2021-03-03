class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = ["" for _ in range(numRows)]
        r, rev = 0, False
        for i in range(len(s)):
            a[r] += str(s[i])
            if numRows > 1:
                if r == numRows - 1:
                    rev = True
                if r == 0:
                    rev = False
                r = r-1 if rev else r+1
        ans = ""
        for i in a:
            ans = ans + i
        return ans

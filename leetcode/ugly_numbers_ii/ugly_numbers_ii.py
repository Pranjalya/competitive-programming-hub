class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i,j,k=0,0,0
        ans = [1]
        while(len(ans)<n):
            ans.append(min([ans[i]*2,ans[j]*3,ans[k]*5]))
            if ans[-1]==ans[i]*2:
                i += 1
            if ans[-1]==ans[j]*3:
                j += 1
            if ans[-1]==ans[k]*5:
                k += 1
        return ans[-1]
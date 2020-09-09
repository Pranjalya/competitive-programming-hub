class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        it = [0]*len(primes)
        ans = [1]
        while(len(ans)<n):
            ans.append(min([ans[it[i]]*primes[i] for i in range(len(primes))]))
            for i in range(len(primes)):
                if ans[-1]==ans[it[i]]*primes[i]:
                    it[i]+=1
        return ans[-1]
'''
Minimum Deletion Cost to Avoid Repeating Letters

Given a string s and an array of integers cost where cost[i] is the cost of deleting the character i in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

 

Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
'''


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                ans += min(cost[i], cost[i+1])
                cost[i+1] = max(cost[i], cost[i+1])
        return ans
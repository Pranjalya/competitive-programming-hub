import collections

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        g1 = collections.defaultdict(lambda: 0)
        g2 = collections.defaultdict(lambda: 0)
        ans = 0
        for i in nums1:
            g1[i**2] += 1
        for i in nums2:
            g2[i**2] += 1
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                ans += g2[nums1[i]*nums1[j]]
        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                ans += g1[nums2[i]*nums2[j]]
        return ans

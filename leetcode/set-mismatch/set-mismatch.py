class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = None
        s = sum(nums)
        n = len(nums)
        # Find duplicate this way
        # for i in nums:
        #     if nums[abs(i)-1] >= 0:
        #         nums[abs(i)-1] = -nums[abs(i)-1]
        #     else:
        #         d = abs(i)
        # Or find duplicate this way
        d = sum(nums) - sum(set(nums))
        return [d, n*(n+1)//2 - (s - d)]

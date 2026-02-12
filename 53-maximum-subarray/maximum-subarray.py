class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float('-inf')
        sums = 0

        for i in range(len(nums)):
            sums += nums[i]

            mx = max(mx,sums)

            if sums < 0:
                sums = 0
        return mx
        
        
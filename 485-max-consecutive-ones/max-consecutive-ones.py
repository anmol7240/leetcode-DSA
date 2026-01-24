class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        ans = 0

        for i in range(n):
            if nums[i] == 1:
                count += 1
                ans = max(count,ans)
            elif nums[i] != 1:
                count = 0

        return(ans)


        
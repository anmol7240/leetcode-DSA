class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(i+1,len(nums)):
            if (nums[j] != 0 and nums[i] == 0):
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            elif nums[i] != 0:
                i+= 1
        return(nums)


        
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        start = n-k
        end = n-1
        while start< end:
            nums[start] , nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        start = 0
        end = n-k-1
        while start< end:
            nums[start] , nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        start = 0
        end = n-1
        while start< end:
            nums[start] , nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        return(nums)


       
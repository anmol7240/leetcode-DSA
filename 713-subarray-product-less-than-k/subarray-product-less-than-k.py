class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        count = 0
        i = 0
        j = 0
        prod = 1

        while (j<n):
            prod *= nums[j]

            while prod >= k:
                prod //= nums[i]
                i += 1
            
            count += j-i+1
            j += 1
        return(count)
        

        
        

    

 



        
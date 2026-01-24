class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        i = 0
        j = 0

        zeroes = 0
        mx = 0

        while(j<n):
            if nums[j] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[i] == 0:
                    zeroes -= 1
                i += 1
            mx = max(mx,j-i+1)
            j += 1
        return(mx)
            

     
                


        

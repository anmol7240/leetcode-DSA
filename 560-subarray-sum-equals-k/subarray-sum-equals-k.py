class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {0:1}
        count = 0
        prex_sum = 0

        for num in nums:
            prex_sum += num
        
            if (prex_sum-k) in freq:
                count += freq[prex_sum -k]
            
            freq[prex_sum] = freq.get(prex_sum,0) + 1
        
        return count
    
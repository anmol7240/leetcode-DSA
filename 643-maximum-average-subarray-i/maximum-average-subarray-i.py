class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        
        i = 0
        j = 0

        mx = 0
        ans = float('-inf')
        while(j<n):
            mx += nums[j]

            if (j-i+1) < k:
                j += 1
            elif (j-i+1) == k:
                ans = max(mx,ans)
                

                mx -= nums[i]
                i += 1
                j += 1

            
        return(ans/float(k))


       
        
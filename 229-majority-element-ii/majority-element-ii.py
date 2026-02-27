class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        result = []
        n = len(nums)
        count1 = 0
        count2 = 0
        el1 = None
        el2 = None

        for num in nums:

            if count1 == 0 and num != el2:
                el1 = num
                count1 = 1
            elif count2 == 0 and num != el1:
                el2 = num
                count2 = 1
            elif num == el1:
                count1 += 1
            elif num == el2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        if nums.count(el1)>n//3:
            result.append(el1)
        if nums.count(el2)>n//3:
            result.append(el2)
        
        return result 
        
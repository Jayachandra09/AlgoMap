class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        res = []
        while i<len(nums):
            start = nums[i]
            while i<len(nums)-1 and nums[i]+1==nums[i+1]:
                i+=1
            # We will increse the index until it satisfy the condition
            # when the condition fails it directly append the string into the res list
            # when the starting and the ending numbers are not equal it will append the range string when they are equal it will just append the single value
            if start!=nums[i]:
                res.append(str(start)+"->"+str(nums[i]))
            else:
                res.append(str(nums[i]))
            i+=1
        return res


# Problem Link : https://leetcode.com/problems/summary-ranges/description/

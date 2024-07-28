def findClosestNumber(nums):
  closest = nums[0]
  for i in nums:
    if abs(i)<abs(closest):
      closest = i
  if closest<0 and abs(closest) in nums:
    return abs(closest)
  else:
    return closest

nums = [-4,-2,1,4,8]
result = findClosestNumber(nums)
print(result)


#Problem Link : https://leetcode.com/problems/find-closest-number-to-zero/description/


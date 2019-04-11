'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m={}
        for i in range(len(nums)):
            check=target-nums[i]
            if nums[i] in m:
                return  [i,m[nums[i]]]
            else:
                m[check]=i
        return []

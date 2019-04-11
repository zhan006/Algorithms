'''Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre=0
        cur=0
        if len(nums)==0:
            return 0

        while cur<=len(nums)-2  and nums[pre]==nums[cur]:
            cur+=1
            while nums[pre]!=nums[cur]:
                pre+=1
                nums[pre]=nums[cur]
        return pre+1
                
                
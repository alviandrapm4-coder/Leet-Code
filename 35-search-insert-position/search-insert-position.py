class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target < nums[0]:
                return 0
            if len(nums) == 1:
                return 1
            if target > nums[-1]:
                return len(nums)
            if nums[i] < target < nums[i+1]:
                return i+1
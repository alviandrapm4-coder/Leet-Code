class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #alviandrapiero
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            #nums[i] + x = target
            x = target - nums[i]
            if x in hashmap and hashmap[x] != i:
                return [i, hashmap[x]]
        return []
class Solution(object):
    def twoSum(self, nums, target):
        for i in len(nums):
            for j in len(nums):
                if j == i:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
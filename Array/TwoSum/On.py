class Solution(object):
    def twoSum(self, nums, target):
        prevElement = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevElement:
                return [prevElement[diff], i]
            prevElement[n] = i
        return

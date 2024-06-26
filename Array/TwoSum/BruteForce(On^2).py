class Solution(object):
    def twoSum(self, nums, target):
        # Loop through the remaining elements in the list starting from the next index
        for j in range(i + 1, len(nums)):
            # Check if the sum of the current pair equals the target
            if nums[i] + nums[j] == target:
                # If it does, return the indices of the two numbers
                return [i, j]
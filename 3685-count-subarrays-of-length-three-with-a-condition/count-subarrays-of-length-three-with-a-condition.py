class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        # We only need to check consecutive groups of 3 numbers
        for i in range(len(nums) - 2):
            # Check if first + third = middle/2
            if nums[i] + nums[i + 2] == nums[i + 1] / 2:
                count += 1
        return count
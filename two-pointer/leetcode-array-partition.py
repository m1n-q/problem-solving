# https://leetcode.com/problems/array-partition/
# sorted array
class Solution:
    def arrayPairSum(self, nums: list) -> int:
        nums.sort(key=lambda x: -x)
        return sum([nums[i] for i in range(len(nums)) if i % 2])

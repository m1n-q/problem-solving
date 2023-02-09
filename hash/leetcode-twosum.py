# https://leetcode.com/problems/two-sum/
class Solution:
    # bruteforce
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     size = len(nums)
    #     for i in range(size):
    #         for j in range(size):
    #             if i != j and nums[i] + nums[j] == target:
    #                 return i, j;
    
    # Follow-up
    # hash, dictionary
    # two pointer, binary search 로는 어렵다. 정렬하면 원래 인덱스가 망가지기 때문
    def twoSum(self, nums: list, target: int) -> list:
        numsDict = {}
        for i, num in enumerate(nums):
            numsDict[num] = i

        print(numsDict)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numsDict and numsDict[diff] != i:
                return i, numsDict[diff]

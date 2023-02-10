# https://leetcode.com/problems/3sum/
# two pointer
class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        answer = []

        for i in range(len(nums)-1):
            # 왼쪽 부분을 포함하는 답은 앞의 i에서 이미 검출, i 뒤쪽에서만 2개 찾으면 됨
            # 즉. i 는 triplet의 최소값으로 triplet 대표하는 키가 되는 느낌?
            left = i + 1
            right = len(nums) - 1

            while left < right:
                should_be_0 = nums[left] + nums[right] + nums[i]
                if should_be_0 < 0:
                    left += 1
                elif should_be_0 > 0:
                    right -= 1
                else:
                    if (triplet := [nums[i], nums[left], nums[right]]) not in answer:
                        answer.append(triplet)
                    left += 1
                    right -= 1
        return answer

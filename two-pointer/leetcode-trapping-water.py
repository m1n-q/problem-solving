# https://leetcode.com/problems/trapping-rain-water
# two pointer

class Solution:
    @staticmethod
    def trap(height: list) -> int:
        left = 0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right]

        answer = 0
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                answer += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                answer += right_max - height[right]
        return answer

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        size = len(temperatures)
        answer = [0]*size

        i = 0
        while i < size:
            if not stack:
                stack.append((i, temperatures[i]))
                i += 1
                continue
            while i < size and stack[-1][1] >= (temp := (i, temperatures[i]))[1]:
                stack.append(temp)
                i += 1
            while stack and stack[-1][1] < temp[1]:
                popped = stack.pop()
                answer[popped[0]] = temp[0] - popped[0]
        return answer
# leetcode submit region end(Prohibit modification and deletion)


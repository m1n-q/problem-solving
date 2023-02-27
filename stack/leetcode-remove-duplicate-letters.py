from collections import Counter


class Solution:
    def remove_duplicate_letters(self, s: str) -> str:
        counter, stack = Counter(s), []

        for char in s:
            counter[char] -= 1
            if char in stack:
                continue

            while stack \
                    and stack[-1] > char \
                    and counter[stack[-1]]:
                stack.pop()
            stack.append(char)

        return "".join(stack)




# leetcode submit region end(Prohibit modification and deletion)

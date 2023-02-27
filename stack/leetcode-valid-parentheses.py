# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def is_valid(self, s: str) -> bool:

        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue
            if stack[-1] == "(" and char == ")" \
                    or stack[-1] == "{" and char == "}" \
                    or stack[-1] == "[" and char == "]":
                stack.pop()
            else:
                stack.append(char)
        return not bool(stack)
# leetcode submit region end(Prohibit modification and deletion)

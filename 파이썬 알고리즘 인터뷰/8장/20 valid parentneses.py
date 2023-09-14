class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if c == ")" and last != "(":
                    return False
                elif c == "}" and last != "{":
                    return False
                elif c == "]" and last != "[":
                    return False

        return len(stack) == 0

class Solution2:
    def isValid(self, s: str) -> bool:
        parentheses_table = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for c in s:
            if parentheses_table.get(c) is None:
                stack.append(c)

            elif not stack or parentheses_table.get(c) != stack.pop():
                return False

        return len(stack) == 0
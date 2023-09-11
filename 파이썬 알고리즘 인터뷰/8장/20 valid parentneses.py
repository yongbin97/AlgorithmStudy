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

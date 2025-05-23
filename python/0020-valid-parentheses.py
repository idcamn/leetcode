class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for x in s:
            if x in pairs:
                stack.append(x)
            elif len(stack) == 0 or pairs[stack.pop()] != x:
                return False
        return len(stack) == 0
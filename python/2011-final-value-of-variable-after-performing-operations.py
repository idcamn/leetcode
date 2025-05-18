class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for oper in operations:
            if "--" in oper: x -= 1
            elif "++" in oper: x += 1
        return x
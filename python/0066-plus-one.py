class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = ""
        for digit in digits:
            str_digits += str(digit)
        res = list(str(int(str_digits) + 1))
        for i, c in enumerate(res):
            res[i] = int(c)
        return res
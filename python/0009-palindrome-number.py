class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # avoid unnecessary operations for negative numbers
            return False
        check_x = list((str(x)))
        if check_x != list(reversed(check_x)):
            return False
        else:
            return True
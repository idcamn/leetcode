class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = i_max = max(nums)
        while i >= 0:
            if i not in nums:
                return i
            i -= 1
        return i_max + 1
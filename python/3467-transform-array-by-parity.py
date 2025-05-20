class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted([0 if n % 2 == 0 else 1 for n in nums])
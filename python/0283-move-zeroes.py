class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key = lambda n: n == 0)
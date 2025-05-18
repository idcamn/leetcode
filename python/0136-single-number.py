class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = {}
        
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1
        for num in numbers:
            if numbers[num] == 1:
                return num
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goods = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    goods += 1
        return goods
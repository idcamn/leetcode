class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums_shuffled = list()
        for i in range(n):
            nums_shuffled.extend([nums[i], nums[i + n]])
        return nums_shuffled
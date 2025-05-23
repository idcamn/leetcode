class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        d_arr = []
        for n in arr:
            d_arr.append(n)
            if n == 0:
                d_arr.append(n)
        for i in range(len(arr)):
            arr[i] = d_arr[i]
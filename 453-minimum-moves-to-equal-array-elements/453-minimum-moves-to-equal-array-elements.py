class Solution:
    def minMoves(self, nums: List[int]) -> int:
        num_iter = 0
        min_nums = min(nums)
        for el in nums:
            num_iter += el - min_nums
        return num_iter
        
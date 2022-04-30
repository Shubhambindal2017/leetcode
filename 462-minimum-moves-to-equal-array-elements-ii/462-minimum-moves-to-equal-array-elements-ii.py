class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)

        num_iter = 0
        middle = int(len(nums)/2)
        for i in nums[:middle]:
            num_iter += abs(i-nums[middle])
        for i in nums[middle+1:]:
            num_iter += abs(i-nums[middle])
        return num_iter
            
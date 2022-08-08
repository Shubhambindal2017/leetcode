class Solution:
    def jump(self, nums: List[int]) -> int:
        
        i = 0
        j = 0
        res = 0
        
        while j < len(nums)-1:
            farthest = 0
            for k in range(i, j+1):
                farthest = max(farthest, k + nums[k])
            i = j + 1
            j = farthest
            res += 1
        return res
        
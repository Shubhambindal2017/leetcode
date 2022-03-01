class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Applying Kadane's Algorithm
        local_sum = 0
        max_sum = -10**5
        for element in nums:
            local_sum += element
            max_sum = max(max_sum, local_sum) # above for cases like [-1]
            if local_sum < 0:
                local_sum = 0
            
        return max_sum
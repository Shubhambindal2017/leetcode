class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        for i in range(len(nums)):
            first_el = nums[i]
            second_el = target - nums[i]
            if second_el in nums_set:
                return (nums_set[second_el], i)
            else:
                nums_set[first_el] = i
                
        
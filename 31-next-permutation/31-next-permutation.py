class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:

            found_left_pt = False
            for i in range(len(nums)-2, -1, -1):
                if nums[i] < nums[i+1]:
                    found_left_pt = True
                    break

            if not found_left_pt:
                rev_ind_i = i
                rev_ind_j = len(nums)-1

                while(rev_ind_i < rev_ind_j):
                    nums[rev_ind_i], nums[rev_ind_j] = nums[rev_ind_j], nums[rev_ind_i]
                    rev_ind_i +=1
                    rev_ind_j -= 1

            else:
                for j in range(len(nums)-1, -1, -1):
                    if nums[i] < nums[j]:
                        break

                nums[i], nums[j] = nums[j], nums[i]

                rev_ind_i = i+1
                rev_ind_j = len(nums)-1

                while(rev_ind_i < rev_ind_j):
                    nums[rev_ind_i], nums[rev_ind_j] = nums[rev_ind_j], nums[rev_ind_i]
                    rev_ind_i +=1
                    rev_ind_j -= 1

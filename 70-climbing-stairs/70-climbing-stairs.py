def num_ways(array, n):
    if array[n] != -1:
        return array[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        array[n] = num_ways(array, n-1) + num_ways(array, n-2)
        return array[n]
    
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        num_of_ways_to_climb = [-1]*(n+1)
        return num_ways(num_of_ways_to_climb, n)

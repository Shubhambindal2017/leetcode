class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def dfs(num):
            if num in dp:
                return dp[num]
            max_mul = 0 if num == n else  num
            for i in range(1, num):
                mult = dfs(i) * dfs(num-i)
                max_mul = max(max_mul, mult)
                dp[num] = max_mul
            return dp[num]
        return dfs(n)
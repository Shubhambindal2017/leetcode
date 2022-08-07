class Solution:
    def get_lcs_length(self, word1, word2):
        dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
        
    def minDistance(self, word1: str, word2: str) -> int:
        lcs_length = self.get_lcs_length(word1, word2)
        return len(word1) + len(word2) - 2 * lcs_length
        
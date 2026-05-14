class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        
        # dp[i][j] = Max ASCII sum of common subsequence of s1[:i] and s2[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Total ASCII sum of both strings
        total_sum = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]:
                    # Match found: add ASCII value to the diagonal result
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    # No match: take the best result from top or left
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Result is total sum minus twice the common sum (since it's in both strings)
        return total_sum - 2 * dp[n][m]

#tarronnsaiadabala
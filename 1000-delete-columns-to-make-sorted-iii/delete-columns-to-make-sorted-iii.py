class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        cols = len(strs[0])
        
        # dp[j] stores the length of the longest valid 
        # subsequence of columns ending at column j.
        dp = [1] * cols
        
        for j in range(cols):
            for k in range(j):
                # Check if column j can follow column k for ALL rows
                can_follow = True
                for i in range(n):
                    if strs[i][k] > strs[i][j]:
                        can_follow = False
                        break
                
                if can_follow:
                    dp[j] = max(dp[j], dp[k] + 1)
        
        # Max kept columns
        max_kept = max(dp) if dp else 0
        
        # Minimum deletions = Total columns - Max kept columns
        return cols - max_kept

#tarronnsaiadabala
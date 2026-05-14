class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initial counts for n = 1
        # aba: patterns using 2 colors (e.g., RYR)
        # abc: patterns using 3 colors (e.g., RYG)
        aba = 6
        abc = 6
        
        for _ in range(1, n):
            # Calculate next row counts based on transition rules
            # New ABA count = 3 * current_aba + 2 * current_abc
            # New ABC count = 2 * current_aba + 2 * current_abc
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD
            
            aba, abc = next_aba, next_abc
            
        return (aba + abc) % MOD

#tarronnsaiadabala
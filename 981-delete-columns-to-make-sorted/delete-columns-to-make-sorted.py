class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Number of rows (n) and number of columns (length of strings)
        rows = len(strs)
        cols = len(strs[0])
        
        deletion_count = 0
        
        # Check each column one by one
        for c in range(cols):
            for r in range(rows - 1):
                # Compare current character with the one in the next row
                if strs[r][c] > strs[r + 1][c]:
                    # Column is not lexicographically sorted
                    deletion_count += 1
                    # Stop checking this column and move to the next one
                    break
                    
        return deletion_count

#tarronnsaiadabala
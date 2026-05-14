class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Row prefix sums
        rows = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                rows[r][c+1] = rows[r][c] + grid[r][c]
                
        # Column prefix sums
        cols = [[0] * n for _ in range(m + 1)]
        for c in range(n):
            for r in range(m):
                cols[r+1][c] = cols[r][c] + grid[r][c]

        def is_magic(r, c, k):
            # Use first row as the reference target sum
            target = rows[r][c+k] - rows[r][c]
            
            # Check rows
            for i in range(1, k):
                if rows[r+i][c+k] - rows[r+i][c] != target:
                    return False
            
            # Check columns
            for j in range(k):
                if cols[r+k][c+j] - cols[r][c+j] != target:
                    return False
            
            # Check main diagonal
            diag1 = 0
            for i in range(k):
                diag1 += grid[r+i][c+i]
            if diag1 != target:
                return False
            
            # Check anti-diagonal
            diag2 = 0
            for i in range(k):
                diag2 += grid[r+i][c+k-1-i]
            if diag2 != target:
                return False
            
            return True

        # Try possible side lengths k from largest to smallest
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
                        
        return 1

#tarronnsaiadabala
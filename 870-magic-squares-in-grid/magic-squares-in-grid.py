class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0
        
        def is_magic(r, c):
            # 1. Check if center is 5 (Optimization)
            if grid[r+1][c+1] != 5:
                return False
            
            # 2. Check for distinct numbers 1-9
            vals = [
                grid[r][c], grid[r][c+1], grid[r][c+2],
                grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]
            ]
            if sorted(vals) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            
            # 3. Check Rows sum (we already know center is part of row2)
            if sum(grid[r][c:c+3]) != 15: return False
            if sum(grid[r+1][c:c+3]) != 15: return False
            if sum(grid[r+2][c:c+3]) != 15: return False
            
            # 4. Check Columns sum
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15: return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15: return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15: return False
            
            # 5. Check Diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15: return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15: return False
            
            return True

        count = 0
        # Iterate through all possible top-left corners of a 3x3 subgrid
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1
                    
        return count

#tarronnsaiadabala
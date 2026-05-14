class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can_cross(day):
            # Mark flooded cells up to 'day'
            # 1-based to 0-based conversion
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1
            
            queue = deque()
            visited = [[False] * col for _ in range(row)]
            
            # Start BFS from all land cells in the top row
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited[0][c] = True
            
            while queue:
                r, c = queue.popleft()
                
                # If we reached the bottom row
                if r == row - 1:
                    return True
                
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and \
                       not visited[nr][nc] and grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            
            return False

        # Binary Search for the last possible day
        low, high = 1, len(cells)
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_cross(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans

#tarronnsaiadabala
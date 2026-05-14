class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        # 1. Simulate Gravity (Stones fall to the right)
        for r in range(m):
            # empty_pos tracks the rightmost available cell
            empty_pos = n - 1
            for c in range(n - 1, -1, -1):
                if boxGrid[r][c] == "*":
                    # Obstacle found: next stone must stop above it
                    empty_pos = c - 1
                elif boxGrid[r][c] == "#":
                    # Stone found: move it to empty_pos
                    boxGrid[r][c] = "."
                    boxGrid[r][empty_pos] = "#"
                    empty_pos -= 1
        
        # 2. Rotate 90 Degrees Clockwise
        # New dimensions will be n x m
        rotated_box = [["" for _ in range(m)] for _ in range(n)]
        for r in range(m):
            for c in range(n):
                # Standard rotation formula: (r, c) -> (c, m - 1 - r)
                rotated_box[c][m - 1 - r] = boxGrid[r][c]
                
        return rotated_box

#tarronnsaiadabala
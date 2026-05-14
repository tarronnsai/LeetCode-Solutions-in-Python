class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2
        
        # Determine the range for binary search
        low = min(y for x, y, l in squares)
        high = max(y + l for x, y, l in squares)
        
        # Binary search for the y-coordinate
        # 100 iterations provide precision far beyond 10^-5
        for _ in range(100):
            mid = (low + high) / 2
            area_below = 0
            
            for x, y, l in squares:
                if mid <= y:
                    continue
                elif mid >= y + l:
                    area_below += l * l
                else:
                    area_below += l * (mid - y)
            
            if area_below < target:
                low = mid
            else:
                high = mid
                
        return low

#tarronnsaiadabala
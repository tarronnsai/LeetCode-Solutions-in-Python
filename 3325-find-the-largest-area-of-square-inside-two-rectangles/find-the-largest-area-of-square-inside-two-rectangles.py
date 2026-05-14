class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the boundaries of the intersection of rectangle i and j
                # Bottom-left of intersection
                inter_x1 = max(bottomLeft[i][0], bottomLeft[j][0])
                inter_y1 = max(bottomLeft[i][1], bottomLeft[j][1])
                
                # Top-right of intersection
                inter_x2 = min(topRight[i][0], topRight[j][0])
                inter_y2 = min(topRight[i][1], topRight[j][1])
                
                # Calculate width and height of the intersection
                width = inter_x2 - inter_x1
                height = inter_y2 - inter_y1
                
                # If width and height are positive, they intersect
                if width > 0 and height > 0:
                    # The largest square in this rectangle is the smaller of its dimensions
                    side = min(width, height)
                    if side > max_side:
                        max_side = side
                        
        return max_side * max_side

#tarronnsaiadabala
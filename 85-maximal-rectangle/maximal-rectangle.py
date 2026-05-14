class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * (cols + 1) # Extra 0 at end to flush the stack
        max_area = 0
        
        for row in matrix:
            # 1. Update histogram heights for the current row
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # 2. Find the largest rectangle in the current histogram (heights)
            # Using a monotonic increasing stack
            stack = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area

#tarronnsaiadabala
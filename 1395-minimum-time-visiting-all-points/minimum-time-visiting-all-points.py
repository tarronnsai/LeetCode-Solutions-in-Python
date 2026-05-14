class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        
        # Iterate through the points and calculate distance between pairs
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            
            # The time to move between two points is the max difference 
            # between their x and y coordinates.
            total_time += max(abs(x2 - x1), abs(y2 - y1))
            
        return total_time

#tarronnsaiadabala
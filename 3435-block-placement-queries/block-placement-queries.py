import bisect
from typing import List

class SegmentTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (2 * self.n)

    def update(self, index: int, value: int):
        # Point update: update the gap value at a specific coordinate index
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left: int, right: int) -> int:
        # Range maximum query in the interval [left, right]
        res = 0
        left += self.n
        right += self.n + 1  # Make the range inclusive
        while left < right:
            if left & 1:
                res = max(res, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                res = max(res, self.tree[right])
            left //= 2
            right //= 2
        return res


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Determine the maximum coordinate domain dynamically
        max_coord = 0
        for q in queries:
            max_coord = max(max_coord, q[1])
            
        # Set a boundary limit slightly beyond the maximum possible query coordinate
        limit = max_coord + 2
        
        seg_tree = SegmentTree(limit + 1)
        obstacles = [0, limit]
        
        # Initially, the entire line up to the limit is a single large gap
        seg_tree.update(limit, limit)
        
        results = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                # Find where to place the new obstacle to keep the list sorted
                idx = bisect.bisect_left(obstacles, x)
                L = obstacles[idx - 1]
                R = obstacles[idx]
                
                obstacles.insert(idx, x)
                
                # Update the segment tree with the split gaps
                seg_tree.update(R, R - x)
                seg_tree.update(x, x - L)
                
            elif q[0] == 2:
                x, sz = q[1], q[2]
                
                # Find the closest obstacle to the left of or equal to x
                idx = bisect.bisect_right(obstacles, x)
                L = obstacles[idx - 1]
                
                # Case 1: Max gap within fully enclosed obstacle bounds up to L
                max_gap = seg_tree.query(0, L)
                
                # Case 2: The remaining partial gap extending from L to x
                max_gap = max(max_gap, x - L)
                
                results.append(max_gap >= sz)
                
        return results

#tarronnsaiadabala
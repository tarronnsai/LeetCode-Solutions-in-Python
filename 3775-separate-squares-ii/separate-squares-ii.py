import collections

class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs)
        self.count = [0] * (4 * self.n)
        self.length = [0.0] * (4 * self.n)

    def update(self, v, tl, tr, l, r, add):
        if l > r:
            return
        if l == tl and r == tr:
            self.count[v] += add
        else:
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), add)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add)
        
        if self.count[v] > 0:
            self.length[v] = self.xs[tr + 1] - self.xs[tl]
        else:
            if tl != tr:
                self.length[v] = self.length[2 * v] + self.length[2 * v + 1]
            else:
                self.length[v] = 0.0

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()
        for x, y, l in squares:
            events.append((y, 1, x, x + l))     # Bottom edge
            events.append((y + l, -1, x, x + l)) # Top edge
            xs.add(x)
            xs.add(x + l)
        
        events.sort()
        sorted_xs = sorted(list(xs))
        x_map = {val: i for i, val in enumerate(sorted_xs)}
        st = SegmentTree(sorted_xs)
        
        # First pass: Calculate total union area
        total_area = 0.0
        prev_y = events[0][0]
        for y, type, x1, x2 in events:
            total_area += st.length[1] * (y - prev_y)
            st.update(1, 0, len(sorted_xs) - 2, x_map[x1], x_map[x2] - 1, type)
            prev_y = y
        
        # Second pass: Find the y-coordinate that splits the area
        target_area = total_area / 2.0
        current_area = 0.0
        st = SegmentTree(sorted_xs) # Reset tree
        prev_y = events[0][0]
        
        for y, type, x1, x2 in events:
            slice_area = st.length[1] * (y - prev_y)
            if current_area + slice_area >= target_area:
                # The line is within this vertical slice
                needed = target_area - current_area
                return prev_y + (needed / st.length[1])
            
            current_area += slice_area
            st.update(1, 0, len(sorted_xs) - 2, x_map[x1], x_map[x2] - 1, type)
            prev_y = y
            
        return float(prev_y)

#tarronnsaiadabala
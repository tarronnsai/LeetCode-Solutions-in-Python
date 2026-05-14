class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_max_consecutive(bars):
            if not bars:
                return 1
            # Sort the bars to find consecutive sequences
            bars.sort()
            max_gap = 1
            current_gap = 1
            
            for i in range(1, len(bars)):
                # If current bar is consecutive to the previous one
                if bars[i] == bars[i-1] + 1:
                    current_gap += 1
                else:
                    max_gap = max(max_gap, current_gap)
                    current_gap = 1
            
            # The gap size created is (number of removed consecutive bars + 1)
            return max(max_gap, current_gap) + 1

        # Find the maximum possible height and width of a gap
        max_h = get_max_consecutive(hBars)
        max_v = get_max_consecutive(vBars)
        
        # The side length of the largest square is the minimum of the two
        side = min(max_h, max_v)
        
        return side * side
#tarronnsaiadabala
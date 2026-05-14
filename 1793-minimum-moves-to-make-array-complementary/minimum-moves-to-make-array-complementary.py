class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # diff[s] stores the change in moves needed if the target sum is s
        diff = [0] * (2 * limit + 2)
        n = len(nums)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # Ensure a is the smaller value for easier logic
            low, high = min(a, b), max(a, b)
            
            # Range logic:
            # 1. Default: 2 moves for any sum in [2, 2*limit]
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            
            # 2. Range for 1 move: [low + 1, high + limit]
            # We subtract 1 move from the default 2 in this range
            diff[low + 1] -= 1
            diff[high + limit + 1] += 1
            
            # 3. Exactly 0 moves: sum == a + b
            # We subtract another 1 move from the 1 move already calculated
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            
        # Sweep through the difference array to find the minimum moves
        ans = n  # Maximum possible moves is n
        current_moves = 0
        for s in range(2, 2 * limit + 1):
            current_moves += diff[s]
            if current_moves < ans:
                ans = current_moves
                
        return ans
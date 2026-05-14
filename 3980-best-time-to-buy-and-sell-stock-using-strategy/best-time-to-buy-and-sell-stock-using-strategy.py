class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        original_profit = sum(s * p for s, p in zip(strategy, prices))
        
        # We need to find max gain from the modification.
        # gain_hold[i] = profit change if we set strategy[i] to 0
        # gain_sell[i] = profit change if we set strategy[i] to 1
        gain_hold = [-s * p for s, p in zip(strategy, prices)]
        gain_sell = [(1 - s) * p for s, p in zip(strategy, prices)]
        
        half_k = k // 2
        
        # Initial gain for window starting at index 0
        # First half_k elements are set to Hold, next half_k are set to Sell
        current_gain = sum(gain_hold[:half_k]) + sum(gain_sell[half_k:k])
        max_gain = max(0, current_gain)
        
        # Slide the window from 1 to n - k
        for i in range(1, n - k + 1):
            # Window moves from [i-1 ... i+k-2] to [i ... i+k-1]
            
            # 1. Element at (i-1) leaves the 'Hold' section
            current_gain -= gain_hold[i - 1]
            
            # 2. Element at (i + half_k - 1) moves from 'Sell' section to 'Hold' section
            current_gain -= gain_sell[i + half_k - 1]
            current_gain += gain_hold[i + half_k - 1]
            
            # 3. Element at (i + k - 1) enters the 'Sell' section
            current_gain += gain_sell[i + k - 1]
            
            max_gain = max(max_gain, current_gain)
            
        return original_profit + max_gain

#tarronnsaiadabala
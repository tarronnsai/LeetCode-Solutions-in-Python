class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        #tarronnsaiadabala
        # 1. Sort in descending order to pick largest values first
        happiness.sort(reverse=True)
        
        total_happiness = 0
        
        # 2. Iterate through the first k elements
        for i in range(k):
            # The current child's happiness is reduced by the number of turns passed (i)
            # Use max(0, ...) to ensure happiness doesn't go negative
            current_val = max(0, happiness[i] - i)
            
            # If we hit a child whose happiness has dropped to 0, 
            # all subsequent children (who have lower base happiness) will also be 0.
            if current_val == 0:
                break
                
            total_happiness += current_val
            
        return total_happiness
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort the costs in descending order
        cost.sort(reverse=True)
        
        total_cost = 0
        
        # Iterate through the sorted list
        for i in range(len(cost)):
            # Every 3rd candy (index 2, 5, 8, ...) is free.
            # So, we only add the cost if it's NOT the 3rd candy in the group.
            if i % 3 != 2:
                total_cost += cost[i]
                
        return total_cost

#tarronnsaiadabala
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #tarronn
        # Map to store: {number_value: its_index}
        prev_map = {}
        
        for i, n in enumerate(nums):
            complement = target - n
            
            # If the complement exists in our map, we've found the solution
            if complement in prev_map:
                return [prev_map[complement], i]
            
            # Otherwise, add the current number to the map
            prev_map[n] = i
            
        return [] # Should not be reached based on constraints
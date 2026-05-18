class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        
        while True:
            # Check if the array is already non-decreasing
            is_non_decreasing = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    is_non_decreasing = False
                    break
            
            if is_non_decreasing:
                return operations
            
            # Find the adjacent pair with the minimum sum (leftmost tie-breaker)
            min_sum = float('inf')
            target_index = -1
            
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    target_index = i
            
            # Replace the pair with their sum
            nums[target_index] = min_sum
            nums.pop(target_index + 1)
            
            operations += 1

#tarronnsaiadabala
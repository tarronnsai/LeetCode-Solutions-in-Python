class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # While the current number is a valid positive integer within the 
            # range of indices AND it's not already at its correct home...
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap it to its correct home.
                # Note: target_idx is nums[i] - 1
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # Second pass: find the first index that doesn't match the value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all spots are filled correctly, the answer is n + 1
        return n + 1
#tarronnsaiadabala
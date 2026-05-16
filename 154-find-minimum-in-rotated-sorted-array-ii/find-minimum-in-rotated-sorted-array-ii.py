class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[high]:
                # Minimum must be in the right half
                low = mid + 1
            elif nums[mid] < nums[high]:
                # Minimum must be at mid or in the left half
                high = mid
            else:
                # Tricky case: nums[mid] == nums[high]
                # Safely reduce the search space by shifting the right bound
                high -= 1
                
        return nums[low]

#tarronnsaiadabala
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum must be in the right half.
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the minimum is either at mid or in the left half.
            else:
                high = mid
                
        # When low == high, it points to the minimum element
        return nums[low]

#tarronnsaiadabala
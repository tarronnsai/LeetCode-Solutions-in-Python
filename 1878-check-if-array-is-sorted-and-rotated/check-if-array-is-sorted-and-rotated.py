class Solution:
    def check(self, nums: List[int]) -> bool:
        count_drops = 0
        n = len(nums)
        
        for i in range(n):
            # Compare current element with the next element (circularly)
            if nums[i] > nums[(i + 1) % n]:
                count_drops += 1
                
            # If we detect more than 1 drop, it cannot be a rotated sorted array
            if count_drops > 1:
                return False
                
        return True

#tarronnsaiadabala
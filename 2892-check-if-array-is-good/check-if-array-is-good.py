class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if not nums:
            return False
        #tarronnsaiadabala    
        # 1. n is the maximum element in the array
        n = max(nums)
        
        # 2. base[n] must have length n + 1
        if len(nums) != n + 1:
            return False
        
        # 3. Use a frequency map (or sorted comparison) to check elements
        # Sorting is efficient here given the small constraints (length <= 100)
        nums.sort()
        
        # Construct the expected base[n] array
        expected = list(range(1, n + 1)) + [n]
        
        return nums == expected
#tarronnsaiadabala
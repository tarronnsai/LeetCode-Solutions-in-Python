class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        
        # Step 1: Insert all possible prefixes of numbers in arr1 into a hash set
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10  # Remove the last digit to get the next prefix
        
        longest_prefix_len = 0
        
        # Step 2: For each number in arr2, check its prefixes against our set
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    # If found, check if its length is greater than our current maximum
                    # We can use len(str(num)) or math.log10, but since num <= 10^8, 
                    # standard string conversion is perfectly fine.
                    longest_prefix_len = max(longest_prefix_len, len(str(num)))
                    break  # Since we go from longest prefix to shortest, we can break early for this number
                num //= 10
                
        return longest_prefix_len

#tarronnsaiadabala
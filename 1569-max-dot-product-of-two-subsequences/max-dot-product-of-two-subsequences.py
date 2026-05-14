class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        # dp[i][j] will store max dot product for nums1[:i] and nums2[:j]
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Product of the current two elements
                current_product = nums1[i-1] * nums2[j-1]
                
                # Option 1: Current product + best product of previous subsequences
                # We use max(0, ...) because we can start a fresh subsequence if 
                # previous sum was negative.
                option1 = current_product + max(0, dp[i-1][j-1])
                
                # Option 2: Skip nums1[i-1]
                option2 = dp[i-1][j]
                
                # Option 3: Skip nums2[j-1]
                option3 = dp[i][j-1]
                
                dp[i][j] = max(option1, option2, option3)
                
        return dp[n][m]

#tarronnsaiadabala
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        len1, len2 = len(nums1), len(nums2)
        
        # Traverse both arrays using two pointers
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                return nums1[i]  # Found the smallest common element
            elif nums1[i] < nums2[j]:
                i += 1           # Value in nums1 is smaller, move pointer i forward
            else:
                j += 1           # Value in nums2 is smaller, move pointer j forward
                
        return -1  # No common element found

#tarronnsaiadabala
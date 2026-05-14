class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
                continue
            
            # Find the position of the rightmost '0' bit in p
            # We want to flip the 1-bit immediately to the left of this 0-bit
            # to minimize ans[i].
            
            # Example p = 11 (binary 1011)
            # Bits:  8 4 2 1
            # Val:   1 0 1 1
            # Rightmost 0 is at bit with value 4.
            # Bit to flip is the one to the left (value 2).
            # ans = 11 - 2 = 9.
            
            # Find the mask for the first 0-bit from the right
            mask = 1
            while p & mask:
                mask <<= 1
            
            # The bit to unset is mask >> 1
            ans.append(p ^ (mask >> 1))
            
        return ans

#tarronnsaiadabala
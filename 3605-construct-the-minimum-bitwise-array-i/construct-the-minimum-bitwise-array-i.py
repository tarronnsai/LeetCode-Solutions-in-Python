class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
                continue
            
            # Find the position of the rightmost 0 in p
            # We want to flip the bit to the left of the rightmost 0
            # Example p=11 (1011). Rightmost 0 is at bit 2 (val 4).
            # The bit to flip is at bit 1 (val 2). 
            # 11 - 2 = 9. 9 OR 10 = 11.
            
            # Find the position of the first '0' bit from the right
            target_bit = 1
            while p & target_bit:
                target_bit <<= 1
            
            # The bit to remove from p is target_bit >> 1
            ans.append(p ^ (target_bit >> 1))
            
        return ans

#tarronnsaiadabala
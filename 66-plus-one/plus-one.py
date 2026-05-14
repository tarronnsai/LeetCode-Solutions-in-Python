class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the rightmost digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                # No carry needed, increment and exit
                digits[i] += 1
                return digits
            
            # Current digit is 9, so it becomes 0 and carry moves left
            digits[i] = 0
            
        # If we exit the loop, it means we had a carry out of the most significant digit
        # Example: [9, 9, 9] became [0, 0, 0], so we return [1, 0, 0, 0]
        return [1] + digits

#tarronnsaiadabala
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_abs_sum = 0
        min_abs_value = float('inf')
        negative_count = 0
        
        for row in matrix:
            for val in row:
                # Add absolute value to total sum
                abs_val = abs(val)
                total_abs_sum += abs_val
                
                # Track the smallest absolute value in the matrix
                if abs_val < min_abs_value:
                    min_abs_value = abs_val
                
                # Count negatives
                if val < 0:
                    negative_count += 1
        
        # If there's an even number of negatives, we can make them all positive
        if negative_count % 2 == 0:
            return total_abs_sum
        
        # If odd, one value must remain negative; we choose the smallest one
        return total_abs_sum - 2 * min_abs_value

#tarronnsaiadabala
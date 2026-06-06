class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Calculate the total sum of the entire array
        right_sum = sum(nums)
        left_sum = 0
        answer = []
        
        for num in nums:
            # The current element is no longer to the right of itself
            right_sum -= num
            
            # Compute the absolute difference
            answer.append(abs(left_sum - right_sum))
            
            # The current element will now be to the left of the next element
            left_sum += num
            
        return answer
#tarronnsaiadabala
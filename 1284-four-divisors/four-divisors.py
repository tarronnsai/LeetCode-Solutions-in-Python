class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        
        for num in nums:
            divisors = set()
            # Iterate up to the square root of the number
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                
                # Optimization: If we exceed 4 divisors, stop checking this number
                if len(divisors) > 4:
                    break
            
            # If the number has exactly four divisors, add their sum to total
            if len(divisors) == 4:
                total_sum += sum(divisors)
                
        return total_sum

#tarronnsaiadabala
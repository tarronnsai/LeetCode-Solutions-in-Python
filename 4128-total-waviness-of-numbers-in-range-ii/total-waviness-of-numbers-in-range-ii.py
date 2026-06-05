class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(X: int) -> int:
            if X < 100:
                return 0
            
            s = str(X)
            n = len(s)
            
            # memoization state: (idx, prev, p_prev, is_less, is_started)
            # Returns a tuple: (total_waviness_contribution, total_valid_ways)
            @lru_cache(None)
            def dp(idx, prev, p_prev, is_less, is_started):
                if idx == n:
                    # We reached the end of the number. Base case.
                    # Return 0 waviness contribution, but 1 valid way formed.
                    return 0, 1
                
                limit = 9 if is_less else int(s[idx])
                ans_waviness = 0
                ans_ways = 0
                
                for curr in range(limit + 1):
                    next_less = is_less or (curr < limit)
                    
                    if not is_started:
                        if curr == 0:
                            # Still leading zeros, nothing changes
                            wavi, ways = dp(idx + 1, -1, -1, next_less, False)
                        else:
                            # First non-zero digit placed
                            wavi, ways = dp(idx + 1, curr, -1, next_less, True)
                    else:
                        # We have already started forming a valid sequence
                        # Check if 'prev' is a valid peak or valley relative to 'p_prev' and 'curr'
                        is_wavy = False
                        if p_prev != -1:
                            if p_prev < prev > curr:   # Peak
                                is_wavy = True
                            elif p_prev > prev < curr: # Valley
                                is_wavy = True
                        
                        wavi, ways = dp(idx + 1, curr, prev, next_less, True)
                        
                        # If 'prev' is a wavy point, it contributes to all valid ways down this path
                        if is_wavy:
                            ans_waviness += ways
                            
                    ans_waviness += wavi
                    ans_ways += ways
                    
                return ans_waviness, ans_ways

            # Extract just the total waviness accumulated
            return dp(0, -1, -1, False, False)[0]

        return solve(num2) - solve(num1 - 1)
#tarronnsaiadabala
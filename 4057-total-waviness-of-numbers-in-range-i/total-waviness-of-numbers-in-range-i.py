class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
    
        for n in range(num1, num2 + 1):
        # Convert number to string to easily access neighbors
            s = str(n)
            length = len(s)
        
        # Numbers with fewer than 3 digits have 0 waviness
            if length < 3:
                continue
            
            current_num_waviness = 0
        # Start from the second digit and end at the second to last
            for i in range(1, length - 1):
                prev_digit = int(s[i-1])
                curr_digit = int(s[i])
                next_digit = int(s[i+1])
            
            # Check for Peak
                if curr_digit > prev_digit and curr_digit > next_digit:
                    current_num_waviness += 1
            # Check for Valley
                elif curr_digit < prev_digit and curr_digit < next_digit:
                    current_num_waviness += 1
        
            total_waviness += current_num_waviness
        
        return total_waviness

#tarronnsaiadabala
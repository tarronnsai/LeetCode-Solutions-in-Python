class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur_penalty = 0
        min_penalty = 0
        best_hour = 0
        
        for i, char in enumerate(customers):
            # If we move the closing time past a 'Y', penalty goes down
            if char == 'Y':
                cur_penalty -= 1
            # If we move it past an 'N', penalty goes up
            else:
                cur_penalty += 1
            
            # If this is the lowest penalty we've seen, mark the hour
            # We use < (not <=) because we want the EARLIEST hour
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                best_hour = i + 1
                
        return best_hour

#tarronnsaiadabala
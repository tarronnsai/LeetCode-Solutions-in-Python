class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Map of (bottom_left, bottom_right) -> [possible_tops]
        transitions = defaultdict(list)
        for pattern in allowed:
            transitions[pattern[:2]].append(pattern[2])
            
        memo = {}

        def can_build(current_row):
            # If we reached the top (only one block), we are done
            if len(current_row) == 1:
                return True
            
            if current_row in memo:
                return memo[current_row]
            
            # Generate all possible next rows
            possible_next_rows = []
            
            def get_next_level_combinations(idx, next_row_acc):
                # If we've processed the whole current_row, we have a complete next_row
                if idx == len(current_row) - 1:
                    possible_next_rows.append("".join(next_row_acc))
                    return
                
                pair = current_row[idx:idx+2]
                if pair in transitions:
                    for top in transitions[pair]:
                        next_row_acc.append(top)
                        get_next_level_combinations(idx + 1, next_row_acc)
                        next_row_acc.pop() # Backtrack

            get_next_level_combinations(0, [])
            
            # Try building the pyramid for each possible next row
            for next_row in possible_next_rows:
                if can_build(next_row):
                    memo[current_row] = True
                    return True
            
            memo[current_row] = False
            return False

        return can_build(bottom)

#tarronnsaiadabala
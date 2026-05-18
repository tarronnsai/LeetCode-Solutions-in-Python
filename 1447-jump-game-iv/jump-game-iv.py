class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # Group indices by their value
        value_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            value_to_indices[val].append(i)
            
        # BFS initialization
        queue = deque([(0, 0)]) # (current_index, steps)
        visited = {0}
        
        while queue:
            curr, steps = queue.popleft()
            
            # If we reached the last index, return the steps
            if curr == n - 1:
                return steps
                
            # Rule 3: Jump to indices with the same value
            val = arr[curr]
            if val in value_to_indices:
                for neighbor in value_to_indices[val]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
                # Crucial Optimization: Clear the entry so we don't look 
                # through these indices again for other elements with the same value.
                del value_to_indices[val]
                
            # Rule 1 & 2: Walk forward or backward
            for neighbor in (curr + 1, curr - 1):
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
                    
        return 0

#tarronnsaiadabala
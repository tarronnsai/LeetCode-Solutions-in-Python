class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        visited = {start}
        
        while queue:
            curr = queue.popleft()
            
            # If we find a target index with value 0, return True
            if arr[curr] == 0:
                return True
            
            # Calculate the two potential jump destinations
            forward = curr + arr[curr]
            backward = curr - arr[curr]
            
            # Check if forward jump is valid and unvisited
            if forward < n and forward not in visited:
                visited.add(forward)
                queue.append(forward)
                
            # Check if backward jump is valid and unvisited
            if backward >= 0 and backward not in visited:
                visited.add(backward)
                queue.append(backward)
                
        return False

#tarronnsaiadabala
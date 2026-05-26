class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # If the destination itself is blocked, we can never reach it
        if s[n - 1] == '1':
            return False
            
        # Queue will store indices that are reachable and can be jumped FROM
        queue = deque([0])
        # far_reached tracks the highest index we've considered jumping TO.
        # This prevents us from re-processing the same indices.
        far_reached = 0
        
        while queue:
            curr = queue.popleft()
            
            # The window of indices we can jump to from 'curr'
            start = max(curr + minJump, far_reached + 1)
            end = min(curr + maxJump, n - 1)
            
            for j in range(start, end + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    queue.append(j)
            
            # Update far_reached to the end of the current window we just scanned
            far_reached = max(far_reached, end)
            
        return False

#tarronnsaiadabala
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        # memo[i] will store the maximum indices we can visit starting from index i
        memo = [-1] * n
        
        def dfs(i: int) -> int:
            # If already calculated, return the cached result
            if memo[i] != -1:
                return memo[i]
            
            max_visited = 1 # We can always at least visit the starting index itself
            
            # 1. Explore valid jumps to the right (i + x)
            for x in range(1, d + 1):
                j = i + x
                if j >= n or arr[j] >= arr[i]:
                    break # Blocked by the array boundary or a taller/equal element
                max_visited = max(max_visited, 1 + dfs(j))
                
            # 2. Explore valid jumps to the left (i - x)
            for x in range(1, d + 1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break # Blocked by the array boundary or a taller/equal element
                max_visited = max(max_visited, 1 + dfs(j))
                
            memo[i] = max_visited
            return max_visited

        # We can start at any index, so find the maximum among all possible starting positions
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
            
        return ans

#tarronnsaiadabala
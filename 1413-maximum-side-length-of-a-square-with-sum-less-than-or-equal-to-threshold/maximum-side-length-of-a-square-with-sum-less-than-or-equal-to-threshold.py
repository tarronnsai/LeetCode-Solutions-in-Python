class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # 1. Build the 2D Prefix Sum Table
        # pref[i][j] is the sum of mat[0...i-1][0...j-1]
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pref[i][j] = (mat[i-1][j-1] + 
                             pref[i-1][j] + 
                             pref[i][j-1] - 
                             pref[i-1][j-1])
        
        def get_sum(r1, c1, r2, c2):
            return (pref[r2+1][c2+1] - 
                    pref[r1][c2+1] - 
                    pref[r2+1][c1] + 
                    pref[r1][c1])

        ans = 0
        # 2. Iterate through all possible bottom-right corners (i, j)
        for i in range(m):
            for j in range(n):
                # Try to see if a square of size (ans + 1) fits here
                # The top-left corner would be (i - ans, j - ans)
                if i - ans >= 0 and j - ans >= 0:
                    current_sum = get_sum(i - ans, j - ans, i, j)
                    if current_sum <= threshold:
                        ans += 1
                        
        return ans

#tarronnsaiadabala
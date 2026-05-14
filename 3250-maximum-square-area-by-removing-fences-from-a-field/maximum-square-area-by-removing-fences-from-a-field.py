class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # Add the boundary fences that cannot be removed
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        
        # Function to get all possible distances between any two fences
        def get_all_distances(fences):
            fences.sort()
            distances = set()
            num_fences = len(fences)
            for i in range(num_fences):
                for j in range(i + 1, num_fences):
                    distances.add(fences[j] - fences[i])
            return distances

        # Get all possible side lengths for horizontal and vertical directions
        h_distances = get_all_distances(hFences)
        v_distances = get_all_distances(vFences)
        
        # Find the intersection of both sets to find possible square side lengths
        common_distances = h_distances.intersection(v_distances)
        
        if not common_distances:
            return -1
        
        # Find the maximum side length
        max_side = max(common_distances)
        
        MOD = 10**9 + 7
        return (max_side * max_side) % MOD
#tarronnsaiadabala
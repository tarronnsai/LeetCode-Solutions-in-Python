class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Step 1: Sort the candidates to handle duplicates and enable pruning
        candidates.sort()
        
        def backtrack(start: int, target: int, path: list[int]):
            # Base Case: Target met
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # Early Pruning: If the element is greater than the remaining target, 
                # all subsequent elements will also be greater (since array is sorted).
                if candidates[i] > target:
                    break
                
                # Skip duplicate elements to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include the current element
                path.append(candidates[i])
                
                # Move to the next element (i + 1) since each number can only be used once
                backtrack(i + 1, target - candidates[i], path)
                
                # Backtrack: Remove the element before the next iteration
                path.pop()
                
        backtrack(0, target, [])
        return res

#tarronnsaiadabala
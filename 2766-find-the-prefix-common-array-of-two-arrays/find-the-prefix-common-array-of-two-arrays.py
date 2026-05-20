class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = []
        seen_count = {}
        common_so_far = 0
        
        for i in range(n):
            # Track the element from array A
            seen_count[A[i]] = seen_count.get(A[i], 0) + 1
            if seen_count[A[i]] == 2:
                common_so_far += 1
                
            # Track the element from array B
            seen_count[B[i]] = seen_count.get(B[i], 0) + 1
            if seen_count[B[i]] == 2:
                common_so_far += 1
                
            # Append the running total for the current index
            C.append(common_so_far)
            
        return C

#tarronnsaiadabala
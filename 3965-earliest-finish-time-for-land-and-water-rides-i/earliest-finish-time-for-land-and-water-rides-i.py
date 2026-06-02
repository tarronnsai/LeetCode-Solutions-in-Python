class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
    
    # Initialize with infinity so we can easily track the minimum time
        min_finish_time = float('inf')
    
    # Iterate through every possible pair of land and water rides
        for i in range(n):
            for j in range(m):
                # --- Case 1: Land ride i first, then Water ride j ---
                land_finish = landStartTime[i] + landDuration[i]
                water_start = max(land_finish, waterStartTime[j])
                case1_total = water_start + waterDuration[j]
            
                # --- Case 2: Water ride j first, then Land ride i ---
                water_finish = waterStartTime[j] + waterDuration[j]
                land_start = max(water_finish, landStartTime[i])
                case2_total = land_start + landDuration[i]
            
                # Keep track of the absolute minimum finish time found so far
                min_finish_time = min(min_finish_time, case1_total, case2_total)
            
        return min_finish_time

#tarronnsaiadabala
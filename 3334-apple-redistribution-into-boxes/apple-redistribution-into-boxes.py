class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # 1. Get the total number of apples to be boxed
        total_apples = sum(apple)
        
        # 2. Sort capacities in descending order to use largest boxes first
        capacity.sort(reverse=True)
        
        boxes_used = 0
        for cap in capacity:
            # 3. Add a box and subtract its capacity from total_apples
            total_apples -= cap
            boxes_used += 1
            
            # 4. If all apples are boxed, stop
            if total_apples <= 0:
                break
                
        return boxes_used

#tarronnsaiadabala
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()
        
        # Min-heap for available room indices
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        # Min-heap for busy rooms: (end_time, room_index)
        busy_rooms = []
        
        # Track meeting count for each room
        room_usage = [0] * n
        
        for start, end in meetings:
            # 1. Move rooms that have finished their meetings to free_rooms
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            # 2. Assign the meeting to a room
            if free_rooms:
                # Use the lowest-numbered free room
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
                room_usage[room] += 1
            else:
                # No room is free; wait for the one that finishes earliest
                earliest_end, room = heapq.heappop(busy_rooms)
                duration = end - start
                new_end = earliest_end + duration
                heapq.heappush(busy_rooms, (new_end, room))
                room_usage[room] += 1
        
        # 3. Find the room with the most meetings
        max_meetings = -1
        result_room = 0
        for i in range(n):
            if room_usage[i] > max_meetings:
                max_meetings = room_usage[i]
                result_room = i
                
        return result_room

#tarronnsaiadabala
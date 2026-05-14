class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # initially, person 0 and firstPerson know the secret
        knows_secret = [False] * n
        knows_secret[0] = True
        knows_secret[firstPerson] = True
        
        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        i = 0
        m = len(meetings)
        while i < m:
            curr_time = meetings[i][2]
            # Group all meetings happening at the same time
            pool = []
            while i < m and meetings[i][2] == curr_time:
                pool.append(meetings[i])
                i += 1
            
            # Build an adjacency list for the current time frame
            adj = defaultdict(list)
            participants = set()
            for u, v, t in pool:
                adj[u].append(v)
                adj[v].append(u)
                participants.add(u)
                participants.add(v)
            
            # BFS/DFS starting from everyone who already knows the secret
            queue = [p for p in participants if knows_secret[p]]
            learned_this_round = set(queue)
            
            # Standard BFS to spread the secret through the current time's graph
            idx = 0
            while idx < len(queue):
                curr = queue[idx]
                idx += 1
                for neighbor in adj[curr]:
                    if neighbor not in learned_this_round:
                        learned_this_round.add(neighbor)
                        knows_secret[neighbor] = True
                        queue.append(neighbor)
                        
        # Return all indices where knows_secret is True
        return [i for i, known in enumerate(knows_secret) if known]

#tarronnsaiadabala
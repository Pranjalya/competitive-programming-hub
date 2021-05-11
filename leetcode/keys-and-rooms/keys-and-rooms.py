from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        i = 0
        q = deque()
        q.append(i)

        while len(q) > 0:
            i = q.popleft()
            visited.add(i)
            for k in rooms[i]:
                if k not in visited:
                    q.append(k)

        if visited == set(range(len(rooms))):
            return True
        return False
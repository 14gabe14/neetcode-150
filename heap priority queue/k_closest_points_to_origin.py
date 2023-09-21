import heapq

def distance(x, y):
    return (x*x + y*y)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for i in range(len(points)):
            heapq.heappush(pq, (-distance(*points[i]), i))

            if len(pq) > k:
                heapq.heappop(pq)

        return [points[t[1]] for t in pq]

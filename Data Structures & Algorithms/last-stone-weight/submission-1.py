import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-w for w in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            
            diff = abs(x - y)
            if diff != 0:
                heapq.heappush(max_heap, -diff)
        
        if max_heap:
            return -heapq.heappop(max_heap)
        return 0

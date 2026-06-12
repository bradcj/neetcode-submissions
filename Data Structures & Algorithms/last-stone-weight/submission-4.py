class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stone = max(stones)
        bucket = [0] * (max_stone+1)
        for w in stones:
            bucket[w] += 1
        
        first = second = max_stone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue

            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0: # move second pointer until reach next stone
                j -= 1
            
            if j == 0: # reached end of stones; return leftover
                return first

            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        
        return first
